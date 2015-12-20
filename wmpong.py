#!/usr/bin/env python3
# wmaker_pong.py
# A Window Maker themed Pong clone

import os, pygame, random, math
from pygame.locals import *

# We may use sound later
if not pygame.mixer: print ('Warning, sound disabled')

dir_main = os.path.split(os.path.abspath(__file__))[0]
dir_res = os.path.join(dir_main, 'res')
dir_apps = os.path.join(dir_res, 'apps')
try:
    icons_apps = os.listdir(dir_apps)
except(FileNotFoundError):
    icons_apps = []

size_screen = (1024, 768)

class Paddle(pygame.sprite.Sprite):
    # Initialize the sprite at pos
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        image_path = os.path.join(dir_res, 'paddle.png')
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        # Max speed of the paddle
        self.speed = 8

    # Move the paddle in the motion (-1 for up, 1 for down, 0 for nothing)
    def move(self, motion):
        newpos = self.rect.move((0, motion * self.speed))
        if newpos.top >= 0 and newpos.bottom <= size_screen[1]:
            self.rect = newpos

class Ball(pygame.sprite.Sprite):
    # Initialize the sprite centered at pos and use sound_wall when bouncing
    def __init__(self, pos, sound_wall):
        pygame.sprite.Sprite.__init__(self) #call Sprite initializer
        if len(icons_apps) != 0:
            image_path = os.path.join(dir_apps, random.choice(icons_apps))
        else:
            image_path = os.path.join(dir_res, 'tile.tiff')
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.x, self.y = pos
        # Speed of the ball
        self.speed = 2
        self.xspeed = self.yspeed = 0
        # Set a random direction
        self.direction = random.choice((-60, 120)) + random.uniform(0, 120)
        self.update_xyspeed()
        # Wall bounce sound
        self.sound_wall = sound_wall
    # Set the speed and direction of the ball (0 is right, 90 is up)
    def update_xyspeed(self):
        self.xspeed = self.speed * math.cos(math.radians(self.direction))
        self.yspeed = - self.speed * math.sin(math.radians(self.direction))
    # Move the ball.  Bounce off of walls.
    def update(self):
        new_x, new_y = self.x + self.xspeed, self.y + self.yspeed
        newpos = self.rect.copy()
        newpos.center = (new_x, new_y)
        if newpos.top < 0 or newpos.bottom > size_screen[1]:
            self.yspeed *= -1
            new_y = self.y
            self.sound_wall.play()
        self.x, self.y = new_x, new_y
        self.rect.center = (self.x, self.y)


def main():
    # Initialize
    pygame.init()
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption("WMPong")
    random.seed(None)

    # Create the background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((80, 80, 117))

    # Display the background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Game objects
    clock = pygame.time.Clock()
    paddle_l = Paddle((0, 128))
    paddle_r = Paddle((size_screen[0] - 64, 128))
    ball = None
    allsprites = pygame.sprite.RenderPlain((paddle_l, paddle_r))
    sound_paddle = pygame.mixer.Sound(os.path.join(dir_res, 'sine440.wav'))
    sound_wall = pygame.mixer.Sound(os.path.join(dir_res, 'sine599.3.wav'))
    sound_end = pygame.mixer.Sound(os.path.join(dir_res, 'saw110.wav'))

    running = True
    ball_present = False
    while running:
        clock.tick(60)

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            elif event.type == KEYDOWN and event.key == K_SPACE and not ball_present:
                ball = Ball((size_screen[0] / 2, size_screen[1] / 2), sound_wall)
                allsprites.add(ball)
                ball_present = True
                sound_wall.play()

        # Move the paddles
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            paddle_l.move(-1)
        if keys[K_s]:
            paddle_l.move(1)
        if keys[K_k] or keys[K_UP]:
            paddle_r.move(-1)
        if keys[K_j] or keys[K_DOWN]:
            paddle_r.move(1)

        # Update
        allsprites.update()

        # Goal or bust
        if ball_present:
            # Check for paddle hits
            if ball.rect.colliderect(paddle_l.rect):
                # Increase the speed
                ball.speed += 0.5
                # Set the direction
                diff = paddle_l.rect.centery - ball.rect.centery
                denom = paddle_l.rect.height / 2
                ball.direction = 140 * math.asin(max(min(diff / denom, 1), -1)) / math.pi
                ball.update_xyspeed()
                # Shift to the right of the paddle to avoid multiple collisions
                ball.rect.left = paddle_l.rect.right + 1
                ball.x = ball.rect.centerx
                # Play a sound
                sound_paddle.play()
            elif ball.rect.colliderect(paddle_r.rect):
                # Increase the speed
                ball.speed += 0.5
                # Set the direction
                diff = paddle_r.rect.centery - ball.rect.centery
                denom = paddle_r.rect.height / 2
                ball.direction = 140 * math.asin(max(min(diff / denom, 1), -1)) / math.pi
                ball.direction = 180 - ball.direction
                ball.update_xyspeed()
                # Shift to the left of the paddle to avoid multiple collisions
                ball.rect.right = paddle_r.rect.left - 1
                ball.x = ball.rect.centerx
                # Play a sound
                sound_paddle.play()

            # Check for misses
            if ball.rect.left < 0:
                # paddle_l loses
                ball_present = False
            elif ball.rect.right > size_screen[0]:
                # paddle_r loses
                ball_present = False

            # If the ball is removed, actually remove it
            if not ball_present:
                allsprites.remove(ball)
                ball = None
                sound_end.play()


        # Draw everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

    # Quit
    pygame.quit()

if __name__ == '__main__':
    main()
