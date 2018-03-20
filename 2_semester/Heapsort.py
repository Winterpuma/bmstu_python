#                           Оберган Татьяна
# Программа засекает время пирамидальной сортировки (случайного, отсорт.,
# обратно отсорт. массивов по 3 заданным размерностям массивов.

from tkinter import *
from tkinter import messagebox
from time import time
from random import randint
# start_time = time()

root = Tk()
root.geometry('670x500')
root.title('Heapsort')
color = '#ede3e1'
reddish = '#ba614e'
root['bg'] = color
numbers = '0123456789'

# Генерирует массив случайных чисел размерностью n
def generator(n):
    massiv = []
    for i in range(n):
        massiv.append(randint(0, 1000))
    return massiv


####
# Для сорторовки
def swap(i, j, sqc):                    
    sqc[i], sqc[j] = sqc[j], sqc[i] 

def heapify(end, i, sqc):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and sqc[i] < sqc[l]:   
        max = l   
    if r < end and sqc[max] < sqc[r]:   
        max = r   
    if max != i:   
        swap(i, max, sqc)   
        heapify(end, max, sqc)

# Сортировка
def lets_sort(sqc):
    end = len(sqc)   
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):   
        heapify(end, i, sqc)   
    for i in range(end-1, 0, -1):   
        swap(i, 0, sqc)   
        heapify(i, 0, sqc)
    return sqc
####


# Заполняет поля для проверки корректности работы программы
def sort_checker():
    massiv = generator(10)
    massiv_1 = str(massiv)[1:-1]
    massiv_2 = str(lets_sort(massiv))[1:-1]
    nonsort.delete(0, END)
    nonsort.insert(END, massiv_1)
    sort.delete(0, END)
    sort.insert(END, massiv_2)

def sort_inputed():
    try:
        massiv = list(map(int, nonsort.get().split(',')))
        massiv_2 = str(lets_sort(massiv))[1:-1]
        sort.delete(0, END)
        sort.insert(END, massiv_2)
    except:
        messagebox.showerror('Wrong input',
                                 'Input takes only numbers, commas, spaces.')

# Возвращает время сортировки массива
def sort_time(sqc):
    start_time = time()
    sqc = lets_sort(sqc)
    sorting_time = (time() - start_time)
    ms = int((sorting_time*1000)//1) # миллисекунды
    return sqc, ms

# Основные расчеты для таблицы
# massiv1, massiv2, massiv3 - случайный, отсортированный, отсорт. вниз
def calculate():
    ver = '\n' * 5
    try:
        for i in range(3):
            data = [0]*3
            size = int(n[i].get())
            if size < 1:
                messagebox.showerror('Wrong input',
                                     'Input takes only positive numbers')
                break
            massiv1 = generator(size)
            massiv2, data[1] = sort_time(massiv1)
            massiv3, data[0] = sort_time(massiv2)
            massiv3 = massiv3[::-1]
            massiv, data[2] = sort_time(massiv3)
            print(data)
            n_data[i]['text'] = (str(data[0]) + ver + str(data[1])
                                 + ver + str(data[2]))
    except:
        messagebox.showerror('Wrong input',
                                 'Input takes only numbers')

# Часть демонстрации корректности
Info = Label(root, bg=color, text='Input splited by comma:\n\n\nOutput:'+
             '\n'*7+'Sqc size:')
Info.place(x=10, y=25)
nonsort = Entry(root)
nonsort.place(x=160, y=30, width=260)
sort = Entry(root)
sort.place(x=160, y=70, width=260)
generate = Button(root, text ='Generate and sort', command=sort_checker,
                  bg=reddish)
generate.place(x=500, y=27,width=100)
sort_entry = Button(root, text='Sort', bg=reddish, command=sort_inputed)
sort_entry.place(x=500, y=70, width=100)

# Ввод
n1 = StringVar()
N1 = Entry(root, textvariable=n1)
N1.place(x=135, y=175, width=100)
n2 = StringVar()
N2 = Entry(root, textvariable=n2)
N2.place(x=330, y=175, width=100)
n3 = StringVar()
N3 = Entry(root, textvariable=n3)
N3.place(x=525, y=175, width=100)
n = [n1, n2, n3]


# Таблица
hor = '\t' * 4
ver = '\n' * 5
title = Label(root, text='N1'+hor+'N2'+hor+'N3', bg=color)
title.place(x=170, y=150)
names = Label(root, text='Sorted up'+ver+'Random'+ver+'Sorted down', bg=color)
names.place(x=25, y=250)
n1_data = Label(root, text='', bg=color)
n1_data.place(x=170, y=250)
n2_data = Label(root, text='', bg=color)
n2_data.place(x=370, y=250)
n3_data = Label(root, text='', bg=color)
n3_data.place(x=570, y=250)
n_data = [n1_data, n2_data, n3_data]

go = Button(root, text='GO', bg='#ba614e', command=calculate)
go.place(x=350, y=450, width=50, height=30)

info = Label(root, text='* time in milliseconds\nms = s*10^-3', bg=color)
info.place(x=450, y=445)

