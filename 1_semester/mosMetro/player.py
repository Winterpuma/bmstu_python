"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

from pygame import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (153, 222, 2)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = display.set_mode(size)

display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = time.Clock()

# Прямоугольники
rect_x = 50
rect_y = 50
rect_x_ch = 5
rect_y_ch = 5

up = left = right = down = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    for e in event.get():
        if e.type == QUIT:
            done = True

        if e.type == KEYDOWN and e.key == K_UP:
            up = True
        if e.type == KEYDOWN and e.key == K_DOWN:
            down = True
        if e.type == KEYDOWN and e.key == K_LEFT:
            left = True
        if e.type == KEYDOWN and e.key == K_RIGHT:
            right = True

        if e.type == KEYUP and e.key == K_UP:
            up = False
        if e.type == KEYUP and e.key == K_DOWN:
            down = False
        if e.type == KEYUP and e.key == K_LEFT:
            left = False
        if e.type == KEYUP and e.key == K_RIGHT:
            right = False

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here

    draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    if up:
        rect_y -= rect_y_ch
    if down:
        rect_y += rect_y_ch
    if left:
        rect_x -= rect_x_ch
    if right:
        rect_x += rect_x_ch


    # --- Go ahead and update the screen with what we've drawn.
    display.flip()

    # --- Limit to 60 frames per second
    clock.tick(100)

# Close the window and quit.
quit()