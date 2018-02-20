# Программа расчитывает интеграл методами парабол и правых прямоугольников,
# двумя количествами делений. Находит наименее точный метод
# и высчитывает количество делений, для точности eps.
#                           Оберган Татьяна
# a, b - отрезок
# n1, n2, n - количества делений
# h - шаг для делений
# y - функция
# I1, I2, I3, I4 - результаты методов
# average - среднее из них
# kkk - номер наименее точного метода

a, b = map(int,input('Введите границы отрезка через пробел: ').split(' '))
if a > b:
    a, b = b, a
n1, n2 = map(int, input('N1 N2: ').split(' '))


def f(x):
    y = x*x#x**2+4*x+4
    return y


def parabola(n):
    s = 0
    m = n*2
    h = (b-a)/n
    for i in range(n):
        s += f(a+i*h) + 4*f(a+i*h+h/2) + f(a+i*h+h)
    s *= h/6
    return s


def prav_pr(n):
    s = 0
    h = (b-a)/n
    for i in range(n):
        s += f(a+i*h)
    s *= h
    return s


I1 = parabola(n1)
I2 = parabola(n2)
I3 = prav_pr(n1)
I4 = prav_pr(n2)
I = [I1, I2, I3, I4]
average = sum(I)/4
if I1 != I3 and I2 != I4:
    for i in range(len(I)):
        I[i] = abs(I[i] - average)
    kkk = (I.index(max(I)) + 2)//2
else:
    kkk = 3

print('\n N1, N2:             |', '{}'.format(n1).center(20), '|', '{}'.format(n2).center(20) + '\n' + '-'*69)
print(' Параболы:           |', '{:.5}'.format(I1).center(20), '|', '{:.5}'.format(I2).center(20) + '\n' + '-'*69)
print(' Пр. прямоугольники: |', '{:.5}'.format(I3).center(20), '|', '{:.5}'.format(I4).center(20))

if kkk == 3:
    print('\nВсе методы точны.')
else:
    print('\nСамый не точный метод:', kkk)
    eps = float(input('\nВведите eps: '))
    n = 2
    if kkk == 1:
        while abs(parabola(2*n) - parabola(n)) > eps:
            n *= 2
    elif kkk == 2:
        while abs(prav_pr(2*n) - prav_pr(n)) > eps:
            n *= 2
    print('Точность eps при', n)
