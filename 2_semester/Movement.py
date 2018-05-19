import sys
from pygame import *
from math import sin, cos, pi

clock = time.Clock()
size = width, height = 500, 500
screen = display.set_mode(size)
display.set_caption('Catch Birds')

BLACK = 0,0,0
WHITE = 255, 255, 255
BLUE = 14, 33, 137
GREEN = 44, 144, 44
RED = 144, 44, 44
YELLOW = 204, 204, 44

angle = 0
angle_t = 0    
def triangle(angle, angle_t):
    r = 100
    r_t = 50
    c_x, c_y = 250, 250
    
    center_x = 250 + r*cos(angle)
    center_y = 250 + r*sin(angle)
    
    top_x = center_x + r_t*cos(angle_t)
    top_y = center_y + r_t*sin(angle_t)
    down_l_x = center_x + r_t*cos(angle_t+(2*pi/3)) 
    down_l_y = center_y + r_t*sin(angle_t+(2*pi/3))
    down_r_x = center_x + r_t*cos(angle_t+(4*pi/3))
    down_r_y = center_y + r_t*sin(angle_t+(4*pi/3))

    left_x = (top_x + down_l_x)/2
    left_y = (top_y + down_l_y)/2
    right_x = (top_x + down_r_x)/2
    right_y = (top_y + down_r_y)/2
    down_x = (down_l_x + down_r_x)/2
    down_y = (down_l_y + down_r_y)/2
    
    draw.polygon(screen, BLUE, ((top_x, top_y), (left_x, left_y),
                                  (right_x, right_y)), 0)
    draw.polygon(screen, GREEN, ((down_x, down_y), (left_x, left_y),
                                  (right_x, right_y)), 0)
    draw.polygon(screen, RED, ((down_x, down_y), (down_r_x, down_r_y),
                                  (right_x, right_y)), 0)    
    draw.polygon(screen, YELLOW, ((down_x, down_y), (left_x, left_y),
                                  (down_l_x, down_l_y)), 0)


while 1:
    clock.tick(5)
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    
    angle += pi/32
    angle_t += pi/8
    
    screen.fill(WHITE)
    draw.circle(screen, BLACK, (250, 250), 100, 1)
    triangle(angle, angle_t)
               
    display.flip()
