
from pygame import *

init()
size = [800, 800]
screen = display.set_mode(size)
clock = time.Clock()

shrift = font.Font(None, 20)
label = shrift.render("Карта Москвы", True, [0,55,25])
img = image.load('moscoww.png').convert_alpha()

running = True
while running:
    # проверяем события
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            x, y = mouse.get_pos()
            click = True
        else:
            click = False
    # обновляем значения
    #screen.fill([255, 255, 255])
    #screen.blit(img, [75, 100])
    #screen.blit(label, [75, 30])
    if click:
        draw.line(screen, [0, 25, 100], (x - 5, y), (x + 5, y) )
        draw.line(screen, [0, 222, 10], (x, y - 5), (x, y + 5))





    display.flip()

quit()