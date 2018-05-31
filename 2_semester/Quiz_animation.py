# Контрольная по Python.
# Оберган Татьяна ИУ7-25

from pygame import *
import sys

clock = time.Clock()
size = width, height = 800, 600
screen = display.set_mode(size)
display.set_caption('KR')

WHITE = 255, 255, 255
BLACK = 0, 0, 0
YELLOW = 255, 255, 100
BLUE = 0, 0, 255

UFO_x, UFO_y = 600, 500
UFO_w, UFO_h = 150, 80


while 1:
    clock.tick(5)
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
    
    screen.fill(WHITE)
    draw.line(screen, BLACK, (0, 400), (400, 400), 2)
    draw.line(screen, BLACK, (400, 540), (800, 540), 2)
    draw.line(screen, BLACK, (400, 400),(400, 540), 2) 
    
    # UFO
    draw.ellipse(screen, BLACK, (UFO_x-(UFO_w/2), UFO_y-(UFO_h/2), UFO_w, UFO_h), 2)
    draw.circle(screen, BLACK, (UFO_x, UFO_y-int((5/6)*UFO_h)), int(UFO_h/3), 2)

    UFO_w *= 0.98
    UFO_h *= 0.975
    UFO_x += 3
    UFO_y -= 5

    # House
    draw.rect(screen, BLUE, (270, 80, 20, 100))
    draw.polygon(screen, YELLOW, ((70, 200), (320, 200), (195, 100)))
    draw.rect(screen, BLACK, (70, 200, 250, 200), 2)   

    draw.rect(screen, BLACK, (100, 240, 70, 70), 2)
    draw.rect(screen, BLACK, (220, 300, 70, 70), 2)
    draw.line(screen, BLACK, (100, 275),(170, 275), 2)
    draw.line(screen, BLACK, (220, 335), (290, 335), 2)
    draw.line(screen, BLACK, (135, 275),(135, 310), 2)
    draw.line(screen, BLACK, (255, 335), (255, 370), 2)
               
    display.flip()
