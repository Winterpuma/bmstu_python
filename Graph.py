#         #         #         #         #         #         #         #       .
#             Оберган Татьяна
# shag - шаг
# a - значение переменной
# a0 - первое значение а
# b - конечное значение а
# k - порядковый номер
# eps -
# c - функция
# Mx, Mn - максимум и минимум значения с
# znach - список значений с
# zero - ось Х
# nom - номер символа
# oc - координата оси


a0 = float(input('Введите начальную a: '))
b = float(input('Введите конечную а: '))
shag = float(input('Введите шаг: '))
eps = 1e-5
k = 1
a = a0
Mx, Mn = 0, 0
znach = []

# Шапка таблицы
print()
print('   a    \u254f      c     \u254f  #  ')
print(27 * '-')
# Тело таблницы
while a - eps <= b:
    c = a**7 - a**6 + 8*a**5 - 4*a**4 + 6*a**3 + 2*a*a - 5*a + 1
    Mx = c if ((c > Mx) or (a == a0)) else Mx
    Mn = c if ((c < Mn) or (a == a0)) else Mn
    znach.append(c)
    print('{:4.3f}'.format(a).rjust(7),'\u254f',end = '')
    if abs(c) < 100000:
        print('{:.4f}'.format(c).rjust(11),'\u254f',k)
    else:
        print('{:.3e}'.format(c).rjust(11), '\u254f', k)
    a += shag
    k += 1

print('\n','Max(c) - Min(c) = ','{:f}'.format(Mx - Mn))

# График
zero = False if (Mn>0 or Mx<0) else True
a = a0
# Шапка графика
print('\n'+' '*7+'{:.3f}'.format(Mn),' '*50,'{:.3f}'.format(Mx))
print('    X'+' '*5+'\u2514'+'\u2500'*58+'\u2518')
# Вывод графика
for i in range(k-1):
    nom = int(round(60*(znach[i] - Mn))/(Mx - Mn))
    print('{:4.3f}'.format(a).rjust(8)+'  ',end='')
    if zero:
        oc = int(round(60*(-Mn))/(Mx - Mn))
        if oc > nom:
            if nom == 0:
                print('*'+(oc-2)*' '+'\u2502')
            else:
                print(' '*(nom - 1)+'*'+(oc-nom-1)*' '+'\u2502')
        elif oc < nom:
            print(' '*(oc-1)+'\u2502'+(nom-oc-1)*' '+'*')
        else:
            print(' '*(oc-1)+'*')   
    else:
        print(' '*(nom - 1)+'*')
    a += shag


