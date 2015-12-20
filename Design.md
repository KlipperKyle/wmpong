WMPong - Design
=================

WMPong (short for Window Maker Pong) is a Pong clone that uses Window
Maker tiles as the ball and an elongated Window Maker tile for the
paddles.

The goal is to emulate a Window Maker look and feel and provide some
sense of novelty as application icons bounce across the screen.

Window Maker is a window manager that attempts to emulate the look and
feel of the NeXTStep system of the early 90s.

<http://windowmaker.org/screenshots/NeXT-Retro.png>

Sprites
---------

The basic ingredients are:

- Window Maker background tile (located in
  `/usr/share/WindowMaker/Pixmaps/tile.{tiff,xpm}` on my installation)
- 48x48, 56x56, or 64x64 application icons

We need to bundle as game resources:

- Paddle: elongated tile to be used as the paddles (a stretch factor of
  2 in the vertical direction should be OK)
- Ball
    - Window Maker tiles with application icons on them
    - (optional) Maybe some extra tiles such as screenshots of dockapps or the clip

Sounds
--------

(Optional) Some ideas for sounds:

- Tonic and 5th interval sounds: Bouncing against a paddle plays an A
  (440 Hz) sine wave tone.  Bouncing against the wall plays an E (Major
  5th up).  Losing the ball could play a Major 7th an octave or two
  below the base A.

Game mechanics/rules
----------------------

This game is meant to be played with two people.  <ins>However, the game
can also be played with one person (left hand against right hand).</ins>

### Paddles ###

There are two paddles.  One on the left and one on the right.  The
paddle on the left is controlled with the `W` and `S` keys (up and down
motion).  The paddle on the right is controlled with the up and down
arrow keys <ins>(and `k` and `j` keys like in vim)</ins>.

The initial game state is a blank playing field (background Window
Maker-ish purple) with two paddles.  The game waits for a player to
press the spacebar to launch a ball.

### Ball ###

When a player presses the spacebar, a ball is launched in the middle of
the playing field with a random direction.  (The paddle that the ball is
launched toward is chosen randomly because the direction is random.)

The "ball" is actually a square 64x64 Window Maker application tile
(i.e. tile with a logo on it such as Firefox, Gvim, GNUStep, etc.)

The ball bounces elastically off the vertical edges of the screen.  If
the ball misses a paddle, the player controlling the paddle that missed
looses.  The other player wins.

<del>

<p>If the player hits the ball with the paddle, then the ball speed is
increased slightly.  The direction of the paddle is determined by the
following formula:  (I hope it is right.)</p>

<pre>
    direction = arcsin((paddle_mid_y - ball_mid_y) / paddle_height)
</pre>

</del>

<ins>

<p>If the player hits the ball with the paddle, then the ball speed is
increased slightly.  The direction is set as follows: (I found this
formula by trial and error.)</p>

<pre><code>diff = paddle_l.rect.centery - ball.rect.centery
denom = paddle_l.rect.height / 2
ball.direction = 140 * math.asin(max(min(diff / denom, 1), -1)) / math.pi
ball.update_xyspeed()
</code></pre>

<p>The right paddle simply subtracts the direction from 180 to flip the
direction.</p>

</ins>

To avoid bizarre repeated collisions when the ball collides with the
paddle, the ball's x-coordinate is shifted so that the ball is
immediately adjacent to the paddle.

Each time the ball collides with a paddle, the ball's speed is increased
slightly

Alternative scoring system
----------------------------

(Optional) Implement a counter for each player that increments by one
whenever a player scores and let the players play until one player
reaches a score of 11.  The player who reaches 11 wins.

If there is no counter, the first player who scores wins.

<ins>
<p>The counter was not implemented.  Thus, the first player to score wins.</p>
</ins>

Helpful resources
-------------------

- <http://www.pygame.org/project-py-pong-2040-.html>
