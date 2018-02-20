#                             БД    

from pickle import load, dump

print('1. Создать новую базу данных \n2. Открыть существующую БД')
a = int(input())

f_name = str(input('Введите назвение базы данных: ')) + '.txt'
if a == 1:
    v = [str(input('Введите ключи через пробел: ')).split(' ')]
elif a == 2:
    f = open(f_name, 'rb')
    v = load(f)

def f1():
    for i in v[0]:
        print(i.center(15), end=' ')
    print()
    for i in range(1,len(v)):
        for j in v[0]:
            print(v[i][j].center(15), end=' ')
        print()

def f2():
    el = {}
    for i in v[0]:
        el[i] = str(input('Введите '+i+': '))
    return v.append(el)

def f3():
    a = input('1. Поиск по 1 столбцу\n2. Поиск по двум столбцам\n')
    if a == '1':
        for i in v[0]:
            print(i.center(15),end=' ')
        b = input('\nВведите имя столбца: ')
        c = input('Что ищем: ').lower()
        for i in range(1,len(v)):
            if v[i][b].lower() == c:
                for j in v[0]:
                    print(v[i][j].center(15), end=' ')
                print()
    elif a == '2':
        for i in v[0]:
            print(i.center(15),end=' ')
        b = input('\nВведите имя столбца: ')
        c = input('Что ищем в нем: ').lower()
        d = input('Введите имя второго столбца: ')
        e = input('Что в нем ищем: ').lower()
        for i in range(1,len(v)):
            if v[i][b].lower() == c and v[i][d].lower() == e:
                for j in v[0]:
                    print(v[i][j].center(15), end=' ')
                print()
    else:
        print('Нет такой команды.')

def f4():
    for i in v[0]:
        print(i.center(15),end=' ')
    a = str(input('\nВыберите колонку с цифровым значением: '))
    if a in v[0]:
        st, en = map(float, input('Вводим диапазон чисел через пробел: ').split(' '))
        if st > en: st, en = en, st
        for i in range(1,len(v)):
            if v[i][a].replace('.','',1).replace('-','',1).isdigit():
                if st <= float(v[i][a]) <= en:
                    for j in v[0]:
                        print(v[i][j].center(15),end=' ')
                    print()
    else:
        print('Нет такой колонки.')

def f5():
    for i in v[0]:
        print(i.center(15),end=' ')
    a = str(input('\nНа какую колонку смотрим при удалении: '))
    if a in v[0]:
        b = str(input('С каким элементом: ')).lower()
        for i in range(len(v)-1,0,-1):
            if v[i][a].lower() == b:
                v.pop(i)
    else:
        print('Нет такой колонки.')

while 1:
    print('\n1. Просмотреть все записи', '2. Добавить новую запись',
          '3. Поиск элементов', '4. Цифровой фильтр',
          '5. Удаление по значению', '0. Выход', sep='\n')
    a = input()
    if a == '0': break
    elif a == '1': f1()
    elif a == '2': f2()
    elif a == '3': f3()
    elif a == '4': f4()
    elif a == '5': f5()
    elif a == '6':
        print(v)
    else:
        print('Нет такой команды.')

f = open(f_name, 'wb')
dump(v, f)
f.close()
