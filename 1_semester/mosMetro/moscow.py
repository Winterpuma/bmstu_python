# Проектная работа
# Кодовое имя: Мос Метро
# By: Оберган Татьяна

from pygame import *
import pickle

init()
size = [1100, 800]
screen = display.set_mode(size)


class Button:
    def create_button(self, surface, color, x, y, length, height, width, text, text_color, light, font_size):
        surface = self.draw_button(surface, color, length, height, x, y, width, light)
        surface = self.write_text(surface, text, text_color, length, height, x, y, font_size)
        self.rect = Rect(x,y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y, font_size):
        myFont = font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width, light):
        if light:
            for i in range(1,10):
                s = Surface((length+(i*2),height+(i*2)))
                s.fill(color)
                alpha = (255/(i+2))
                if alpha <= 0:
                    alpha = 1
                s.set_alpha(alpha)
                draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
                surface.blit(s, (x-i,y-i))
        draw.rect(surface, color, (x,y,length,height), 0)
        draw.rect(surface, (190,190,190), (x,y,length,height), 1)
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print("Some button was pressed!")
                        return True
        return False

## Цвета
BLUE = (1, 184, 238)
GREY = (233, 233, 233)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## Открываем станции
with open('info.pickle', 'rb') as f:
    info = pickle.load(f)

img_mos_map = image.load('moscoww.png').convert_alpha()
img_metro = image.load('metro.png').convert_alpha()
img_play = image.load('testmetro.png').convert_alpha()
btn_start = Button()
btn_train = Button()
btn_back = Button()
btn_all = Button()
btn_choose = Button()
btn_play_line = Button()
btn_fast = btn_normal = btn_long = Button()


menu = True
pl_metro = tr_metro = line = game = pace = False


## Главное меню: Играть и Тренировка
def gl_menu():
    screen.fill(GREY)
    screen.blit(img_mos_map, [200, 50])
    btn_start.create_button(screen, GREY, 450, 300, 200, 70, 0, 'Играть', BLUE, 1, 35)
    btn_train.create_button(screen, GREY, 450, 400, 200, 70, 0, 'Тренировка', BLUE, 1, 30)
    display.flip()


## Меню выбора игры
def play_metro():
    screen.fill(WHITE)
    screen.blit(img_play, [0, 0])
    btn_back.create_button(screen, GREY, 740, 90, 300, 50, 0, 'Назад', BLUE, 0, 30)
    btn_all.create_button(screen, GREY, 740, 300, 300,50, 0, 'Все станции', BLUE, 0, 30)
    btn_choose.create_button(screen, GREY, 740, 400, 300, 50, 0, 'Выбрать линию', BLUE, 0, 30)
    display.flip()


## Выбираем количество вопросов
def play_pace(vse):
    screen.fill(WHITE)
    screen.blit(img_play, [0, 0])
    btn_back.create_button(screen, GREY, 740, 90, 300, 50, 0, 'Назад', BLUE, 0, 30)
    btn_fast.create_button(screen, GREY, 740, 300, 300, 50, 0, 'Быстро        (10)', BLUE, 0, 30)
    btn_normal.create_button(screen, GREY, 740, 400, 300, 50, 0, 'Нормально (25)', BLUE, 0, 30)
    btn_long.create_button(screen, GREY, 740, 500, 300, 50, 0, 'Долго           (50)', BLUE, 0, 30)
    display.flip()
        


## Список линий для тренировки
def train_metro():
    screen.fill(WHITE)
    screen.blit(img_metro, [0, 0])
    btn_back.create_button(screen, GREY, 790, 20, 300, 50, 0, 'Назад', BLUE, 0, 30)
    y = 100
    global lines_btns
    lines_btns = []
    for i in range(len(info)):
        j = info[i]['name']
        j = Button()
        lines_btns.append(j)
        j.create_button(screen, info[i]['color'], 790, y, 300, 50,0, info[i]['name'], WHITE, 0, 23)
        y += 60
    display.flip()


## Отдельно выбранная линия в тренировке
def train_line(number):
    screen.fill(WHITE)
    screen.blit(img_metro, [0, 0])
    btn_back.create_button(screen, GREY, 790, 20, 300, 50, 0, 'Назад', BLUE, 0, 30)
    btn_play_line.create_button(screen, info[number]['color'], 790, 90, 300, 50, 0, info[number]['name'], WHITE, 0, 20)
    global stations_btns
    stations_btns = []
    if len(info[number]['stations'])> 13:
        x_width = 25
    else:
        x_width = 50
    z = 140
    for i in info[number]['stations']:
        j = i[0]
        j = Button()
        stations_btns.append(j)
        j.create_button(screen, GREY, 790, z, 300, x_width, 0, i[0], (0, 0, 0), 0, 20)
        z += x_width
    display.flip()


    
running = True
gl_menu()
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == MOUSEBUTTONDOWN:
            #print(mouse.get_pos())
            if menu:
                if btn_start.pressed(mouse.get_pos()):
                    menu, pl_metro = False, True
                    play_metro()
                if btn_train.pressed(mouse.get_pos()):
                    menu, tr_metro = False, True
                    train_metro()
            elif pl_metro:
                if btn_back.pressed(mouse.get_pos()):
                    pl_metro, menu = False, True
                    gl_menu()
                if btn_all.pressed(mouse.get_pos()):
                    pl_metro, pace = False, True
                    play_pace(1)
                if btn_choose.pressed(mouse.get_pos()):
                    pl_metro, pace = False, True
                    play_pace(0)
            elif pace:
                if btn_back.pressed(mouse.get_pos()):
                    pace, pl_metro = False, True
                    play_metro()
            elif tr_metro:
                if btn_back.pressed(mouse.get_pos()):
                    tr_metro, menu = False, True
                    gl_menu()
                else:
                    for i, g in enumerate(lines_btns):
                        if g.pressed(mouse.get_pos()):
                            station_num = i
                            tr_metro, line = False, True
                            train_line(i)
            elif line:
                if btn_back.pressed(mouse.get_pos()):
                    line, tr_metro = False, True
                    train_metro()
                else:
                    for i, g in enumerate(stations_btns):
                        if g.pressed(mouse.get_pos()):
                            screen.blit(img_metro, [0, 0])
                            draw.circle(screen, BLACK, info[station_num]['stations'][i][1], 6)
                            display.flip()
                
                            

quit()
