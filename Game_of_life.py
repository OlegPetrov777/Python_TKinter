from tkinter import *
import tkinter
from copy import deepcopy
import random
import time


size = 600  # РАЗМЕР ПОЛЯ
but = 150
a = 10  # РАЗМЕР КЛЕТКИ
line = int(size / a) # КОЛ-ВО КЛЕТОК В КАЖДОМ РЯДУ ИЛИ СТОЛБЦЕ
on_off = 1
t = 0.1
b = [3, None, None, None]
s = [2, 3, None, None, None]
party_on = 0
color = 'white'

root = tkinter.Tk()
c = Canvas(width=size, height=size + but, bg='black')
c.pack()

field = [[0 for i in range(line)] for j in range(line)]  # многомерный массив с 0 - НАЧАЛЬНОЕ ПОЛЕ
field_life = [[random.randint(0, 1) for i in range(line)] for j in range(line)]  # такой же как фиелд, но с рандомными 1

for i in range(line):  # рисую сетку из линий
    c.create_line(0, i * a, size, i * a, fill="#1C1C1C")
    c.create_line(i * a, 0, i * a, size, fill="#1C1C1C")


def mouse(event):
    global a
    x = event.x // a
    y = event.y // a
    field_life[y][x] = 1
    rect = c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill="white", outline="black",
                              tag="life")


def mode_1():
    global field
    global field_life
    field = [[0 for i in range(line)] for j in range(line)]  # многомерный массив с 0 - НАЧАЛЬНОЕ ПОЛЕ
    field_life = [[random.randint(0, 1) for i in range(line)] for j in range(line)]
    c.delete('life')


def mode_2():
    global field
    global field_life
    field = [[0 for i in range(line)] for j in range(line)]  # многомерный массив с 0 - НАЧАЛЬНОЕ ПОЛЕ
    field_life = [[1 if i == line // 2 or j == line // 2 else 0 for i in range(line)] for j in range(line)]
    c.delete('life')


def mode_3():
    global field
    global field_life
    field = [[0 for i in range(line)] for j in range(line)]  # многомерный массив с 0 - НАЧАЛЬНОЕ ПОЛЕ
    field_life = [[1 if not (i * j) % 22 else 0 for i in range(line)] for j in range(line)]
    c.delete('life')


def time_p():
    global t
    t += 0.05


def time_m():
    global t
    if t >= 0.05:
        t -= 0.05


def pause():
    global on_off
    on_off = 0


def start():
    global on_off
    on_off = 1

    
def clear():
    global field
    global field_life
    field = [[0 for i in range(line)] for j in range(line)]
    field_life = [[0 for i in range(line)] for j in range(line)]
    c.delete('life')
    
    
def rool_1():
    global b
    global s
    b = [3, None, None, None]
    s = [2, 3, None, None, None]


def rool_2():
    global b
    global s
    b = [1, 2, 3, 4]
    s = [5, 6, 7, 8, 4]

    
def party_mod():
    global party_on
    party_on += 1

    
def red():
    global color
    color = '#FF4949'

    
def green():
    global color
    color = '#75FC3B'
    
    
def blue():
    global color
    color = '#49FAFF'
    
    
def white():
    global color
    color = 'white'    
    
    
def rect():
    global field_life
    global line
    for i in range(line//4, (line//4)*3):
        for j in range(line//4, (line//4)*3):
            field_life[j][i] = 1
            c.create_rectangle(i * a, j * a, (i + 1) * a, (j + 1) * a, fill=color, outline="black", tag="life")

            
def circle():
    global field_life
    global line
    a = line//3.5
    b = line//3.5
    r = line //8
    EPSILON = 2.2
    for y in range(line):
        for x in range(line):
            if abs((x-a)**2 + (y-b)**2 - r**2) < EPSILON**2:
                field_life[y][x] = 1
                c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill=color, outline="black", tag="life")

                
                
def treug():
    global field_life
    global line
    j = (line//2) 
    for i in range(10, line//2):
        j -= 1
        field_life[j][i] = 1
        c.create_rectangle(i * a, j * a, (i + 1) * a, (j + 1) * a, fill=color, outline="black", tag="life")
        
    for i in range(line//2, line-10):
        j += 1
        field_life[j][i] = 1
        c.create_rectangle(i * a, j * a, (i + 1) * a, (j + 1) * a, fill=color, outline="black", tag="life")
    
    for i in range(10, line-10):
        j = (line//2) 
        field_life[j][i] = 1
        c.create_rectangle(i * a, j * a, (i + 1) * a, (j + 1) * a, fill=color, outline="black", tag="life")
        
        
button1 = Button(root, text='1й режим', command=mode_1).place(x=int(size/2)-125, y=size+50)  # тут кнопочки всякие)
button2 = Button(root, text='2й режим', command=mode_2).place(x=int(size/2)-27, y=size+50)  
button3 = Button(root, text='3й режим', command=mode_3).place(x=int(size/2)+70, y=size+50)  

button_t1 = Button(root, text='Скорость -', command=time_p).place(x=int(size/2)-130, y=size+20) 
button_t2 = Button(root, text='Скорость +', command=time_m).place(x=int(size/2)+70, y=size+20) 

button_p = Button(root, text='Пауза', command=pause).place(x=int(size/2)+10, y=size+20)
button_s = Button(root, text='Старт', command=start).place(x=int(size/2)-40, y=size+20)

button_clear = Button(root, text='Очистить поле', command=clear).place(x=int(size/2)-40, y=size+80)
button_rool_1 = Button(root, text='1е правило', command=rool_1).place(x=int(size/2)-130, y=size+80)
button_rool_2 = Button(root, text='2е правило', command=rool_2).place(x=int(size/2)+70, y=size+80)

button_party_mod = Button(root, text='Вечеринка', command=party_mod).place(x=50, y=size+20)
button_red = Button(root, text='Красный', command=red).place(x=50, y=size+50)
button_green = Button(root, text='Зеленый', command=green).place(x=50, y=size+80)
button_blue = Button(root, text='Синий', command=blue).place(x=100, y=size+110)
button_white = Button(root, text='Белый', command=white).place(x=50, y=size+110)

button_rect = Button(root, text='Квадрат', command=rect).place(x=size-110, y=size+20)
button_circle = Button(root, text='Круг', command=circle).place(x=size-110, y=size+50)
button_treug = Button(root, text='Треугольник', command=treug).place(x=size-110, y=size+80)



def check(field_life, x, y):  # функция проверяет окружение клетки (8 дургих клеток)
    global b
    global s
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if field_life[j][i]:  # если вокуруг клетки оказалась живая, то к количеству + 1
                count += 1
    if field_life[y][x]:  # если порверяемая клетка живая, то ее не считаем (- 1)
        count -= 1
        if count == s[0] or count == s[1] or count == s[2] or count == s[3] or count == s[4]:  # если вокруг живой клетки 2 или 3 живых, то она продолжает жить
            return 1
        return 0
    else:
        if count == b[0] or count == b[1] or count == b[2] or count == b[3]:  # если вокруг мертвой клетки 3 живых, то она оживает
            return 1
        return 0


root.bind('<Button-3>', mouse)


def main():
    global field_life
    global on_off
    global patry_on 
    global color
    
    if on_off == 1:
        time.sleep(t)
        c.delete('life')
        for x in range(1, line - 1):
            for y in range(1, line - 1):
                if field_life[y][x]:
                    
                    if party_on % 2 == 0:
                        c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill=color, outline="black",
                                              tag="life")
                    elif party_on % 2 == 1:
                        r = lambda: random.randint(0,255)
                        c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill='#%02X%02X%02X' % (r(),r(),r()), outline="black",
                                              tag="life")
                field[y][x] = check(field_life, x, y)  # анализируем и возможно обновляем текущую клетку
        field_life = deepcopy(field)
        root.after(10, main)
    else:
        root.after(10, main)

main()
root.mainloop()
