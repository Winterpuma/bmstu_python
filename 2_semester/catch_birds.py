# Pygame бежит человечек из примититов, летит птичка, человек сбивает ее count+1
# Создана ночь, солнце, луна.
#                           Оберган Татьяна

from pygame import *
from random import randint
from math import sin, cos, radians
import sys

clock = time.Clock()

def f(x): return round(((x*x)/500) - 2*x) + 500
def bird_fly(x, y):
    if sun['day']: return y
    else: return abs(round(randint(1,3)*sin(x/40) + y + 0.25))
        
# Цвета
WHITE = 255, 255, 255
BLACK = 0, 0, 0
BIRD = 0, 0, 0
SKIN = 0, 0, 0
SUN = 255, 226, 0
SKY = 127, 199, 255
GRASS = 97, 161, 48
SKY_N = 0, 0, 153
GRASS_N = 0, 26, 0
BIRD_N = 153, 255, 153


# Дисплей
size = width, height = 1000, 600
screen = display.set_mode(size)
display.set_caption('Catch Birds')
# Шрифт
font.init()
def_font = font.Font('freesansbold.ttf', 30)

# Передвижение
left = right = jump = False
earth = 200
g = 10 #коэффициент гравитации

# Координаты человеческого центра
man = {'x':500, 'y':200}
catch_count = 0

# Солнце
sun = {'x':0, 'day': True}

# Птицы
st_angle = 31
birds_count = 0
birds_limit = 10 ### макс кол-во птиц
birds = [{'here': False, 'x':0, 'y':0, 'size':20, 'speed':0,
          'fly':st_angle,'direction':1, 'k':1} for i in range(birds_limit)]
spawn_range = spawn_r_s, spawn_r_f = 50, 250
size_range = size_r_s, size_r_f = 20, 35


# Ф-я прорисовки человека
def human(x, y):
    draw.circle(screen, SKIN, (x, y-40), 30)
    draw.line(screen, SKIN, (x, y+10), (x, y+160),20)
    draw.lines(screen, SKIN, 0, ((x-50, y+110), (x, y+1), (x+50, y+110)), 10)
    draw.lines(screen, SKIN, 0, ((x-40, y+280), (x, y+120), (x+40, y+280)),20)

# Ф-я прорисовки птицы по размеру и углу наклона крыльев
def bird(x, y, size, angle):
    x1 = x + size*cos(radians(180-angle))
    x2 = x - size*cos(radians(180-angle))  
    y1 = y - size*sin (radians(angle))
    draw.lines(screen, BIRD, 0, ((x1, y1), (x, y), (x2, y1)), 4)
    draw.lines(screen, BIRD, 0, ((x1, y1), (x, y-4), (x2, y1)), 4)
    draw.circle(screen, BIRD, (x, y-7), 3)

# Ф-я прорисовки светлячков
def bug(x, y):
    size = randint(2, 5)
    draw.circle(screen, BIRD_N, (x, y), size)
    
# Ф-я спавна новых птиц    
def spawn():
    for i in range(len(birds)):
        if not(birds[i]['here']):
            birds[i]['here'] = True
            birds[i]['direction'] = 1 if randint(0,1) else -1
            birds[i]['x'] = -40 if (birds[i]['direction'] == 1) else width+40
            birds[i]['y'] = randint(spawn_r_s, spawn_r_f)
            birds[i]['size'] = randint(size_r_s, size_r_f)
            birds[i]['speed'] = randint(1, 7)
            birds[i]['fly'] = st_angle
            birds[i]['k'] = 1
            break

    
while 1:
    clock.tick(30)
    for e in event.get():
        if e.type == QUIT:
            print('You catched', catch_count, 'birds!!')
            print('Thanks for playing.')
            quit()
            sys.exit()
        # Реагируем на нажатие клавиш
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                left = True
            if e.key == K_RIGHT:
                right = True
            if e.key == K_SPACE:
                if man['y'] == earth: # человек на земле
                    jump = 10
        if e.type == KEYUP:
            if e.key == K_LEFT:
                left = False
            if e.key == K_RIGHT:
                right = False
          
    if sun['x'] > width:
        sun['x'] = -30
        sun['day'] = False if sun['day'] else True
        
    # Фон
    if sun['day']:
        screen.fill(SKY)
        draw.circle(screen, SUN, (sun['x'], f(sun['x'])), 70)
        sun['x'] += 2
        draw.rect(screen, GRASS, [(0, height-200), (width, height)])
        label = def_font.render(str(catch_count), True, BLACK, GRASS)
    else:
        screen.fill(SKY_N)
        draw.circle(screen, WHITE, (sun['x'], f(sun['x'])), 50)
        sun['x'] += 2
        draw.rect(screen, GRASS_N, [(0, height-200), (width, height)])
        label = def_font.render(str(catch_count), True, WHITE, GRASS_N)
        
    # Передвижение человека
    if left and man['x'] > 47: man['x'] -= 7
    if right and man['x'] < 953: man['x'] += 7
    # Прыжок
    if jump > 0:
        man['y'] -= 22
        jump -= 1
    # Сила притяжения
    if ((man['y'] + g) <= earth): man['y'] += g
    elif (man['y'] < earth): man['y'] = earth
    # Человек
    human(man['x'], man['y'])

    # Count    
    textRect = label.get_rect()
    textRect.center = width-100, height-40
    screen.blit(label, textRect)
    
    # Птицы
    # Спаун птиц
    if birds_count < birds_limit:
        more_bugs = 20 if not sun['day'] else 0
        if (randint(0, 100)-more_bugs <= 5):
            birds_count += 1
            spawn()
    # Прорисовка птиц
    for i in birds:
        if i['here']:
            i['y'] = bird_fly(i['x'], i['y'])
            if ((man['x']-25 <= i['x'] <= man['x']+25) and
                (man['y']-65 <= i['y'])):
                catch_count += 1
                birds_count -= 1
                i['here'] = False
                continue
            if (i['fly'] >= 80) or (i['fly'] <= 30):
                i['k'] *= -1
            i['fly'] += 5*i['k']

            if -40 <= i['x'] <= width + 40:
                i['x'] += i['speed']*i['direction']
            else:
                i['x'] = -40 if i['direction'] == 1 else width+40
            if sun['day']:
                bird(i['x'], i['y'], i['size'], i['fly'])
            else:
                bug(i['x'], i['y'])
    display.flip()

