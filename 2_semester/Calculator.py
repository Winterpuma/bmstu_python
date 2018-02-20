#                           Оберган Татьяна
# Калькулятор с графическим интерфейсом, который переводит
# введенные числа в 8-ю с/с и обратно в 10-ю

import proverka # print(proverka.isit_num('2..7')) -> False
from tkinter import *
from tkinter import messagebox

root = Tk()
root.maxsize(width = 225, height = 350)
root.minsize(width = 225, height = 350)
root.title('Калькулятор')
root.withdraw()
root.geometry('+830+200')

# Вывод информации о программе 
def info(): 
    messagebox.showinfo("Информация", "Автор: Татьяна Оберган"+"\n"+
                       "Программа: перевод из восьмиричной с/с в десятичную "+
                       "и наоборот")
def help_me():
    messagebox.showinfo("Помощь", "1. Вводить можно только символы" +
                        "предоставленные в центре   \t    калькулятора для ввода"+
                        "\n" + "2.1 Для перевода из 8сс в 10ю кликните на кнопку"+
                        "'В десятичную'"+"\n"+"2.2 Для перевода из 10сс в 8ю"+
                        "кликните на кнопку 'В восьмиричную'"+"\n"+
                        "3. В поле ввода появится результат")
    
# Перевод из 8 с/с в 10 с/с
def to_ten(): 
    A = ent.get()
    if not proverka.isit_num(A):
        messagebox.showerror("Ошибка", "Введенные символы не число.")
        entry.delete(0, END)
    elif ('8' in A) or ('9' in A):
        messagebox.showerror("Ошибка", "В восьмеричной с/с не может быть" +
                             "чисел 8 и 9")
        entry.delete(0, END)
    else:
        if A[0] == '-':
            sign = -1
            A = A[1:]
        else:
            sign = 1
        result = 0
        chars = str(float(A)).split('.')
        chars[0], chars[1] = list(map(int, chars[0])), list(map(int, chars[1]))
        m = -1
        for i in range(len(chars[0])-1, -1, -1):
            m += 1
            result += chars[0][i]*(8**m)
        m = 0
        for i in range(len(chars[1])):
            m -= 1
            result += chars[1][i]*(8**m)
            
        result *= sign
        entry.delete(0, END)
        entry.insert(END, result)

# Перевод из 10 с/с в 8 с/с    
def to_eight(): 
    A = ent.get()
    if not proverka.isit_num(A):
        messagebox.showerror("Ошибка", "Введенные символы не число.")
        entry.delete(0, END)
    else:
        if A[0] == '-':
            sign = -1
            A = A[1:]
        else:
            sign = 1
        result = 0
        chars = str(float(A)).split('.')
        m = int(chars[0])
        result = ''
        while m >= 8:
            result += str(m % 8)
            m = m // 8
        result += str(m)
        result = result[::-1]
        drob = ''
        n = float('0.' + chars[1])
        count = 0
        while count < 15:
            count += 1
            n *= 8
            drob += str(int(n // 1))
            n = n % 1
            if n == 0.0:
                break
        final = float(result + '.' + drob) * sign
        entry.delete(0, END)
        entry.insert(END, final)


# В поле вставляется символ передаваемый кнопкой
def ins(number): 
    entry.insert(END, number)
    
# Очистка поля
def clear(): 
    entry.delete(0, END)
    
# Стереть последний символ
def backspace():
    entry.delete(len(entry.get())-1, END)

# Меню
m = Menu(root) 
root.config(menu=m)
 
fm = Menu(m)
m.add_cascade(label='Действия',menu=fm)
fm.add_command(label='Очистить поле', command=clear) 
fm.add_command(label='В десятичную', command=to_ten)
fm.add_command(label='В восьмиричную', command=to_eight)
 
hm = Menu(m)
m.add_cascade(label='Справка',menu=hm)
hm.add_command(label='Помощь', command=help_me)
hm.add_command(label='Информация', command=info)

# Управляющая часть и поле ввода
ent = StringVar()
entry = Entry(root, textvariable = ent, justify=RIGHT)
entry.place(x=10, y=70, width=200, height=40)

to_dec = Button(root, text='В десятичную', command = to_ten)
to_dec.place(x=10, y=140)

to_oct = Button(root, text='В восьмиричную', command = to_eight)
to_oct.place(x=100, y=140)

# Кнопки ввода
one = Button(root, text='1', command=lambda: ins('1'))
one.place(x=10, y=200, width=30, height=30)
two = Button(root, text='2', command=lambda: ins('2'))
two.place(x=40, y=200, width=30, height=30)
three = Button(root, text='3', command=lambda: ins('3'))
three.place(x=70, y=200, width=30, height=30)
four = Button(root, text='4', command=lambda: ins('4'))
four.place(x=100, y=200, width=30, height=30)
five = Button(root, text='5', command=lambda: ins('5'))
five.place(x=10, y=230, width=30, height=30)
six = Button(root, text='6', command=lambda: ins('6'))
six.place(x=40, y=230, width=30, height=30)
seven = Button(root, text='7', command=lambda: ins('7'))
seven.place(x=70, y=230, width=30, height=30)
eight = Button(root, text='8', command=lambda: ins('8'))
eight.place(x=100, y=230, width=30, height=30)
nine = Button(root, text='9', command=lambda: ins('9'))
nine.place(x=10, y=260, width=30, height=30)
zero = Button(root, text='0', command=lambda: ins('0'))
zero.place(x=40, y=260, width=30, height=30)
minus = Button(root, text='-', command=lambda: ins('-'))
minus.place(x=70, y=260, width=30, height=30)
dot = Button(root, text='.', command=lambda: ins('.'))
dot.place(x=100, y=260, width=30, height=30)
back = Button(root, text='Back', command=backspace)
back.place(x=150, y=215, width=50, height=30)
cler = Button(root, text='Clear', command=clear)
cler.place(x=150, y=245, width=50, height=30)

root.deiconify()
root.mainloop()
