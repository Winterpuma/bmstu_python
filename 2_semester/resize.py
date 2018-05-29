import sys
from pygame import *

clock = time.Clock()
size = width, height = 500, 500
screen = display.set_mode(size)
display.set_caption('RK')

BLACK = 0, 0, 0
WHITE = 255, 255, 255

x0, y0 = width/2, height/2

w, h = 50, 10
k = 1.2
#rect = [x0-100, y0+10, 200, 20] # Левый верхний, ширина, высота

while 1:
    clock.tick(5)
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    
    screen.fill(WHITE)
    draw.rect(screen, BLACK, [int(x0-(w/2)), int(y0-(h/2)), int(w), int(h)], 1) #draw.ellipse
        
    w *= k
    h *= k

    display.flip()
