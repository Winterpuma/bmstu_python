# Мн-во точек на пл-ти, треугольники

from tkinter import *
from math import ceil

x, y, xy = [], [], []
to_lbl = ''

def AdPnt():
    A = ent.get()
    a = A.split(' ')
    if len(a) == 2 and a[0].replace('-','',1).replace('.','',1).isdigit()\
    and a[1].replace('-','',1).replace('.','',1).isdigit():
        if [float(a[0]), float(a[1])] in xy:
            print('You already entered this dot')
            # messagebox.showinfo("Khm", "You already entered this dot)
        else:
            s = '(' + a[0] + ';' + a[1] + ')'
            a[0], a[1] = float(a[0]), float(a[1])
            x.append(a[0])
            y.append(a[1])
            xy.append(a)
            bx.insert(END, s)
    #else:
        #messagebox.showerror("Error", "You should have two numbers splited by space")
    ent.delete(0, END)


def pix():
    global x_pix, y_pix, x_max, x_min, y_min, y_max
    if len(x) == 1:
        x_pix, y_pix = [250], [250]
    elif len(x) != 1:
        x_max, x_min = max(x), min(x)
        y_max, y_min = max(y), min(y)
        scale = 475 / max(x_max - x_min, y_max - y_min)
        x_pix, y_pix = [], []
        for i in range(len(x)):
            x_pix.append(ceil((x[i] - x_min) * scale)+12)
            y_pix.append(ceil((y_max - y[i]) * scale)+12)

def ansv(d):
    f = {}
    for i in range(d - 2):
        for j in range(i + 1, d - 1):
            for k in range(j + 1, d):
                if (x[i]-x[j])/(x[j]-x[k]) != (y[i]-y[j])/(y[j]-y[k]):
                    vhod, novhod = 0, 0
                    for z in range(d):
                        if z != i and z != j and z != k:
                            x1, x2, x3, x0 = x[i], x[j], x[k], x[z]
                            y1, y2, y3, y0 = y[i], y[j], y[k], y[z]
                            r1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
                            r2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
                            r3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
                            if ((r1 == 0 and max(x1, x2) >= x0 >= min(x1, x2) and max(y1, y2) >= y0 >= min(y1, y2) )
                            or (r2 == 0 and max(x2, x3) >= x0 >=  min(x2, x3) and max(y2, y3) >= y0 >= min(y2, y3))
                            or (r3 == 0 and max(x3, x1) >= x0 >= min(x3, x1)and max(y3, y1) >= y0 >= min(y3, y1))):
                                continue
                            elif (r1 == abs(r1)) == (r2 == abs(r2)) == (r3 == abs(r3)):
                                vhod += 1  # Точка входит в треугольник.
                            else:
                                novhod += 1
                    print(i, j, k, vhod, novhod)
                    f[abs(novhod - vhod)] = str(i) + str(j) + str(k)
    print(f)
    return f[min(f)]

def draw():
    d = len(x)
    gr.delete('all')
    if d == 0:
        print("You should enter at least one dot")
        # messagebox.showerror("Error", "You should enter at least one dot")
    else:
        pix()
        for i in range(d):
            gr.create_rectangle(x_pix[i] - 4, y_pix[i] - 4, x_pix[i] + 4, y_pix[i] + 4, fill='black')
        if d < 3 or x_max == x_min or y_max == y_min:
            print('no poss triangles')
            #messagebox.showinfo("Hmmm..", "No possible triangles")
        elif d == 3 and ((x[0]-x[1])/(x[1]-x[2])) == ((y[0]-y[1])/(y[1]-y[2])): # если на 1 линии
            print('No poss triangles, 3 dots on 1 line')
            # messagebox.showinfo("Hmmm..", "No possible triangles")
        elif d >= 3:
            f = list(map(int, list(ansv(d))))
            for i in f:
                gr.create_rectangle(x_pix[i] - 5, y_pix[i] - 5, x_pix[i] + 5, y_pix[i] + 5, fill='blue')
            gr.create_line(x_pix[f[0]], y_pix[f[0]], x_pix[f[1]], y_pix[f[1]], x_pix[f[2]],
                           y_pix[f[2]], x_pix[f[0]], y_pix[f[0]], fill='blue', width=3)
        

root = Tk()
root.title('Треугольник из точек')
root.maxsize(width = 950, height = 1000)
root.wm_state('zoomed')

lbl = Label(root, text='Введите координаты х и y через пробел: ', font=('Arial', 20))
lbl. place(x = 10, y = 87)

gr = Canvas(root, bg = 'white')
gr.place(x = 10, y = 200, width = 500, height = 500)

rst = StringVar()
ent = Entry(root, bg = 'pink', textvariable = rst)
ent.bind('<Return>', lambda e: AdPnt())
ent.place(x = 550, y = 100, width = 200)


adBtn = Button(root, text = 'Добавить точку', command = AdPnt)
adBtn.place(x = 780, y = 97)

crBtn = Button(root, text = 'Вывести график', command = draw)
crBtn.place(x = 780, y = 200)

bx = Listbox(root, bg = 'white')
bx.place(x = 550, y = 200, width = 200, height = 500)

root.mainloop()
