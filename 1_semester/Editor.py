
s = ['Крупные корпорации хотят ограничить доступ к',
     'информации.Фальшивые новости и',
     'фильтры усложняют нам нахождение своего пути.Интернет хулиганы',
     'глушат вдохновлённые голоса.Получается и наше желание',
     'провести исследование затрудняется',
     'угрозами для нашей безопасности и конфиденциальности.']


def text(sa):
    q = ''
    for i in sa:
        q += i + ' \n'
    return q


def f1(so):
    f = str(input('Удаляемое слово: ')).lower()
    sen = text(so).split('.')
    z = ''
    for i in range(len(sen)):
        slova = sen[i].split(' ')
        for j in range(len(slova) - 1, -1, -1):
            if slova[j].lower() == f:
                slova.pop(j)
            elif slova[j].lower() == '\n' + f:
                slova[j + 1] = '\n' + slova[j + 1]
                slova.pop(j)
        for j in range(len(slova)):
            z += slova[j]
            if j != len(slova) - 1:
                z += ' '
        if i != len(sen) - 1:
            z += '.'
    f = z.split('\n')
    f.pop(len(f) - 1)
    return f


def f2(so):
    f = str(input('Заменяемое слово: '))
    al = str(input('Заменяющее слово: '))
    for i in range(len(so)):
        so[i] = so[i].replace(f, al)
    return s


def f32(so):
    mah = max([len(i) for i in so])
    for i in so:
        print(i.rjust(mah))


def f33(so):
    mah = max([len(i) for i in so])


def f3(so):
    print('Выберите вид выравнивания: \n\t1 по левому краю'
          '\n\t2 по правому краю\n\t3 по ширине')
    c = int(input())
    if c == 1: return print(text(so))
    if c == 2: return f32(so)
    if c == 3: return f33(so)


def f4(so):
    q = ''
    for i in so:
        q += i + '\n'
    ga = q.split('.')  # предложения в массиве
    ga.pop(len(ga)-1)
    l1 = [len(j) for j in ga]  # длины предложений
    f1 = l1.index(max(l1))
    qo = ga[f1]  # макс предложение
    g = (qo.replace(',','').replace(':','').replace('-',' ')).split(' ')#слова макс предложения
    l2 = [len(j) for j in g]  # длины слов
    f2 = l2.index(min(l2))
    slovo = g[f2]  # минимальное слово
    print(slovo)
    if f2 == 0:
        qq = qo.replace(slovo + ' ', '')
    elif f2 == len(g)-1:
        qq = qo.replace(' ' + slovo, '')
    else:
        qq = qo.replace(' ' + slovo + ' ', ' ')
    ga[f1] = qq
    q = ''
    for i in ga:
        q += i + '.'
    return(q.split('\n'))


while True:
    print('\n' + '\n'.join(s), '\n\n')
    print('1 Удалить заданное слово во всем тексте',
          '2 Произвести замену слова на другое',
          '3 Выравнивание и вывод текста',
          '4 Удалить самое короткое слово в самом длинном предложении',
          '5 Выход из программы', sep='\n')
    a = input()
    if a.isdigit():
        a = int(a)
        if a == 1: s = f1(s)
        elif a == 2: s = f2(s)
        elif a == 3: f3(s)
        elif a == 4: s = f4(s)
        elif a == 5: break
        else: print('Команды не существует.')
    else: print('Введите, пожалуйста, номер команды.')
