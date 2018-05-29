import sys
from pygame import *

clock = time.Clock()
size = width, height = 500, 500
screen = display.set_mode(size)
display.set_caption('RK')

while 1:
    clock.tick(5)
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    
    screen.fill(WHITE)
    draw.circle(screen, BLACK, (250, 250), 100, 1)
               
    display.flip()
