WMPong
========

Author:  Kyle Terrien `<kyleterrien at gmail dot com>`

WMPong (short for Window Maker Pong) is a Pong clone that uses Window
Maker tiles as the ball and an elongated Window Maker tile for the
paddles.

The goal is to emulate a Window Maker look and feel and provide some
sense of novelty as application icons bounce across the screen.

Window Maker is a window manager that attempts to emulate the look and
feel of the NeXTStep system of the early 90s.

- [Window Maker screenshot](http://windowmaker.org/screenshots/NeXT-Retro.png)
- [WMPong screenshot](screenshot01.png)

This was a game I wrote for Computer Science 386 (Intro to Game Design).
I am publishing it so others can enjoy it.

Installing/running
--------------------

You will need Pygame installed on Python 3.  I have tested this game on
Arch Linux with Pygame compiled from their source control system.

- [Pygame](http://www.pygame.org/)
- [Pygame source control](https://bitbucket.org/pygame/pygame)
- [Arch Linux PKGBUILD for Pygame](https://aur.archlinux.org/packages/python-pygame-hg/)
- [Another PKGBUILD for Pygame](https://aur.archlinux.org/packages/python-pygame/)

After setting up Pygame, simply run the game:

    python3 wmpong.py

Playing
---------

You will see a screen with two paddles that are shaped like enlongated
tiles.  The paddle on the left is controlled with `W` (for up) and `S`
(for down).  The paddle on the right is controlled with the arrow keys.
(Also, `K` and `J` will move the paddle on the right, just like in vim.)

Take a moment to familiarize yourself with the controls.

Press `<Space>` to start the game.  An application tile (ball) will
appear in the middle of the screen.  Move the paddles to bounce the
application tile off of the paddles.  The application tile will bounce
off of the top and bottom walls.

Each time the tile is hit, it will speed up a little.  The first paddle
to let the application tile slide off of his side of the screen loses.
Generally each game lasts about two minutes.  Press `<Space>` again to
play another game.

WMPong is intended to be played with two players (one for each paddle).
However, it is possible to play a game against oneself.  (This is how I
tested it.)  In either case, the rules are simple: the first paddle to
miss the ball loses; the other paddle wins.

Press `<Esc>` at any time to quit the game.

Hacking
---------

The `res` directory contains the following:

- `paddle.png` - The paddle
- `tile.tiff` - The background of a tile, taken from Window Maker
- `apps-raw/` - A bunch of icons of (hopefully familiar) applications,
  taken from Window Maker's icon cache
- `apps/` - The icons in `apps-raw` overlaid with `tile.tiff`
- `sine440.wav`, `sine599.3.wav`, `saw110.wav` - Simple tone sounds
  generated with Audacity long ago.

To add more application icons, drop them in `res/apps-raw/`.  They must
be 64x64 pixels or smaller.  Then run the shell script:  (You must have
ImageMagick installed.)

    sh make_apps.sh

You may freely delete the `res/apps/` directory before running this
command.

License
---------

Except where noted, WMPong is released by Kyle Terrien under the [GNU
GPLv2](https://www.gnu.org/licenses/gpl-2.0.html).

The tile icon (`tile.tiff`) is from Window Maker, which is distributed
under [GNU GPLv2](https://www.gnu.org/licenses/gpl-2.0.html).
`paddle.png` is an enlongated version of this image.

Application icons are property of their respective owners, distributed
under Fair Use.

(If, for whatever reason, you do not wish your application icons to be
distributed with WMPong, please contact the author.  I am quite
flexible.  Also, if you wish to add/donate application icons, please
contact the author.)

Known bugs
------------

- Pygame crashes when loading certain XPMs (mitigated by converting
  sprites to PNG)
- The screen is not double buffered (I do not know of a way to
  double-buffer the screen in Pygame.)

Bibliography
--------------

- [The `chimp.py` example script](http://www.pygame.org/docs/tut/chimp/ChimpLineByLine.html)
- [Window Maker](http://windowmaker.org/)
- [py-pong](http://www.pygame.org/project-py-pong-2040-.html)
