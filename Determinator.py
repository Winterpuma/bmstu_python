# Программа считает определитель матрицы
#                Оберган Татьяна
# n - порядок матрицы
# o - матрица
# d - определитель
# kill - ошибка ввода
while True:
    n = str(input('Введите порядок матрицы: '))
    if not(str.isdigit(n)):
        print('Ошибка ввода.\n')
    else:
        n = int(n)
        break
kill = 0
o = []
for i in range(n):
    m = list(map(float,input('Введите строку: ').split()))
    o.append(m)

try:
#приводим к треугольному виду
    for k in range(n):
        for i in range(k+1,n):
            a = -(o[i][k]/o[k][k])
            for j in range(k,n):
                o[i][j] += a*o[k][j]
#считаем определитель
    d = 1
    for k in range (n):
        d *= o[k][k]
    print('Определитель равен:','{:.2f}'.format(d))
except(ZeroDivisionError):
    print('Определитель равен нулю.')




