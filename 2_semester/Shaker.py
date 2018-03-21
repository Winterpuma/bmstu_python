from tkinter import *

root = Tk()
root.title('Shaker')
root.geometry('300x120')

def shaker(sqc):
    a = 0
    b = len(sqc) - 1
    while a < b:
        flag = 0
        for i in range(a, b):
            if sqc[i] > sqc[i+1]:
                sqc[i], sqc[i+1] = sqc[i+1], sqc[i]
                flag = i
        b = flag
        flag = 0
        
        for i in range(b, a, -1):
            if sqc[i-1] > sqc[i]:
                sqc[i], sqc[i-1] = sqc[i-1], sqc[i]
                flag = i
        a = flag
    return sqc


def sort():
    sqc = list(map(int, pole.get().split(' ')))
    sorted_sqc = shaker(sqc)
    output.delete(0, END)
    output.insert(END, str(sorted_sqc)[1:-1])

    
pole = Entry(root)
pole.place(x=20, y=30, width=200)
output = Entry(root)
output.place(x=20, y=70, width=200)
go = Button(root, text='GO', command=sort)
go.place(x=250, y=50)

root.mainloop()
