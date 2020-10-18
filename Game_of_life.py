from tkinter import *
import tkinter
from copy import deepcopy
import random
import time


size = 600  # РАЗМЕР ПОЛЯ
but = 150
a = 10  # РАЗМЕР КЛЕТКИ
t = 0.1
line = int(size / a)
on_off = 1
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


button1 = Button(root, text='1й режим', command=mode_1).place(x=int(size/2)-110, y=size+50)  # тут кнопочки всякие)
button2 = Button(root, text='2й режим', command=mode_2).place(x=int(size/2)-27, y=size+50)  # тут кнопочки всякие)
button3 = Button(root, text='3й режим', command=mode_3).place(x=int(size/2)+53, y=size+50)  # тут кнопочки всякие)
button_t1 = Button(root, text='Скорость -', command=time_p).place(x=int(size/2)-130, y=size+20)  # тут кнопочки всякие)
button_t2 = Button(root, text='Скорость +', command=time_m).place(x=int(size/2)+75, y=size+20)  # тут кнопочки всякие)
button_p = Button(root, text='Пауза', command=pause).place(x=int(size/2)+10, y=size+20)
button_s = Button(root, text='Старт', command=start).place(x=int(size/2)-40, y=size+20)


def check(field_life, x, y):  # функция проверяет окружение клетки (8 дургих клеток)
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if field_life[j][i]:  # если вокуруг клетки оказалась живая, то к количеству + 1
                count += 1
    if field_life[y][x]:  # если порверяемая клетка живая, то ее не считаем (- 1)
        count -= 1
        if count == 2 or count == 3:  # если вокруг живой клетки 2 или 3 живых, то она продолжает жить
            return 1
        return 0
    else:
        if count == 3:  # если вокруг мертвой клетки 3 живых, то она оживает
            return 1
        return 0


root.bind('<Button-3>', mouse)


def main():
    global field_life
    global on_off
    if on_off == 1:
        time.sleep(t)
        c.delete('life')
        for x in range(1, line - 1):
            for y in range(1, line - 1):
                if field_life[y][x]:
                    rect = c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill="white", outline="black",
                                              tag="life")
                field[y][x] = check(field_life, x, y)  # анализируем и возможно обновляем текущую клетку
        field_life = deepcopy(field)
        root.after(10, main)
    else:
        root.after(10, main)

main()
root.mainloop()