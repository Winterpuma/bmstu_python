from pygame import *
from math import sin, asin

clock = time.Clock()
size = width, height = 500, 500
screen = display.set_mode(size)
display.set_caption('RK')

WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 150, 147, 142
LG = 200, 200, 200

def f(y): return int(10*sin(y/20)+400)
def f2(y): return int(20*sin(y/30)+400)

length = 100
dots = [i*2+100 for i in range(length)] # по y

while 1:
    clock.tick(5)
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    
    screen.fill(WHITE)
    for i in range(length):
        draw.circle(screen, GREY, (f(dots[i]), dots[i]), 4)
        draw.circle(screen, LG, (f(dots[i]-10), dots[i]), 4)
        
        draw.circle(screen, GREY, (f2(dots[i]), dots[i]), 4)
        draw.circle(screen, LG, (f2(dots[i]-10), dots[i]), 4)
        
        if dots[i] > 0:
            dots[i] -= 5
        else:
            dots[i] = 300 - i%5
                       
    display.flip()
