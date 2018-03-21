from tkinter import *

def answer(res):
    resultat.delete(0, END)
    resultat.insert(END, str(int(res)))

    
def f1():
    num_one = a.get()
    num_two = b.get()
    len_one = len(num_one)
    len_two = len(num_two)
    score = len_one - len_two
    if score != 0:
        if score > 0:
            num_two = ('0'*score) + num_two
        elif score < 0:
            num_one = ('0'*(score*-1)) + num_one
    num_one, num_two = num_one[::-1], num_two[::-1]
    return num_one, num_two

    
def add():
    ostatok = 0
    result = ''
    one, two = f1()
    for i in range(len(one)):
        summa = int(one[i]) + int(two[i]) + ostatok
        ostatok = 0
        if summa > 5:
            ostatok = 1
            summa %= 5
        result += str(summa)
    if ostatok != 0:
        result += ostatok
    answer(result[::-1])

    
def subtract():
    one, two = f1()
    result = ''
    ostatok = 0
    for i in range(len(one)):
        razn = int(one[i]) - int(two[i]) + ostatok
        ostatok = 0
        if razn < 0:
            ostatok = -1
            razn += 5
        result += str(razn)
    answer(result[::-1])
    

root = Tk()

a = StringVar()
ent1 = Entry(root, textvariable = a)
ent1.place(x=10, y=10)

b = StringVar()
ent2 = Entry(root, textvariable = b)
ent2.place(x=10, y=50)

plus = Button(root, command=add, text=' + ')
plus.place(x=10, y=90)

minus = Button(root, command=subtract, text=' - ')
minus.place(x=40, y=90)

resultat = Entry(root)
resultat.place(x=10, y=130)

root.mainloop()
