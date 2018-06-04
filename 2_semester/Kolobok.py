import sys
from pygame import *
from math import sin, cos, pi

clock = time.Clock()
size = width, height = 500, 500
screen = display.set_mode(size)
display.set_caption('Kolobok')

BLACK = 0, 0, 0
WHITE = 255, 255, 255
COLOR = 255, 77, 77

coords = [250, 250]
angle = pi/2
angle2 = pi
angle3 = 0
big_size = 100
size = 50
eye_size = 20

while 1:
    clock.tick(5)
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    
    screen.fill(WHITE)
    draw.circle(screen, BLACK, (250, 250), 100, 5)
    # Центры глаз
    eye_x1 = int(coords[0] + size*cos(angle-(2*pi/3)))
    eye_y1 = int(coords[1] + size*sin(angle-(2*pi/3)))
    eye_x2 = int(coords[0] + size*cos(angle+(2*pi/3)))
    eye_y2 = int(coords[1] + size*sin(angle+(2*pi/3)))
    draw.circle(screen, BLACK, [eye_x1, eye_y1], 5)
    draw.circle(screen, BLACK, [eye_x2, eye_y2], 5)

    eye1 = [[eye_x1 + eye_size*cos(angle3), eye_y1 + eye_size*sin(angle3)],
            [eye_x1 + eye_size*cos(angle3+2*pi/3), eye_y1 + eye_size*sin(angle3+2*pi/3)],
            [eye_x1 + eye_size*cos(angle3+4*pi/3), eye_y1 + eye_size*sin(angle3+4*pi/3)]]

    draw.polygon(screen, BLACK, eye1)

    # улыбка
    draw.arc(screen, BLACK,[coords[0]-50,coords[1]-50, big_size, big_size], angle2, angle2+pi)
    angle4 = angle2+pi/2
    smile_x1 = int(coords[0] + 50*sin(angle4))
    smile_y1 = int(coords[1] + 50*cos(angle4))
    smile_x2 = int(coords[0] + 50*sin(angle4+pi))
    smile_y2 = int(coords[1] + 50*cos(angle4+pi))

    draw.circle(screen, COLOR, [smile_x1, smile_y1], 5)
    draw.circle(screen, COLOR, [smile_x2, smile_y2], 5)
    
    angle += pi/6
    angle2 -= pi/6
    angle3 += pi/6
    
    display.flip()
