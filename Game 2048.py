from tkinter import *
import tkinter
import random

size = 400  # РАЗМЕР ПОЛЯ
a = 100  # РАЗМЕР КЛЕТКИ
line = int(size / a)
SCORE = 0
BEST = 0

root = tkinter.Tk()
c2 = Canvas(width=size + 20, height=105, bg='#F2F2F2')
c2.pack()

# ЛОГОТИП
c2.create_rectangle(11, 5, a + 11, a + 5, fill="#E5D201")  # E5D201  F7ED7E
c2.create_text(62, 53, text="2048", fill='#FFFFFF', font=('impact', 30))

lbl = Label(root)
lbl.configure(font=('asinastra', 20), anchor=tkinter.S, text=("SCORE\n" + str(SCORE)), bg="#BCBCBC", fg="#515151")
lbl.place(x=255, y=15, height=80, width=120)

lbl2 = Label(root)
lbl2.configure(font=('asinastra', 20), anchor=tkinter.S, text=("BEST\n" + str(BEST)), bg="#BCBCBC", fg="#515151")
lbl2.place(x=125, y=15, height=80, width=120)

c = Canvas(width=size, height=size, bg='#FFE5BC')
c.pack()

c3 = Canvas(width=size, height=60, bg='#F2F2F2')
c3.pack()

# Сетка квадратами
for i in range(4):
    for j in range(4):
        c.create_rectangle(j * a, i * a, (j + 1) * a, (i + 1) * a, fill="#B4B4B4", outline="#7B7B7B", width=5)

# ПОЛЕ
field_new = [[0 for i in range(line)] for j in range(line)]


def up():
    global field_new
    global SCORE
    global BEST
    count = 0
    for i in range(4):
        for k in range(4):
            for j in range(4):
                if field_new[j][i] != 0 and j != 0:
                    if field_new[j - 1][i] == 0:
                        field_new[j - 1][i] = field_new[j][i]
                        field_new[j][i] = 0
                        count += 1

                    elif field_new[j - 1][i] == field_new[j][i]:
                        field_new[j - 1][i] = field_new[j][i] * 2
                        field_new[j][i] = 0

                        SCORE = SCORE + field_new[j - 1][i] * 10
                        lbl['text'] = ("SCORE\n" + str(SCORE))

                        count += 1

    if BEST < SCORE:
        BEST = SCORE
        lbl2['text'] = ("BEST\n" + str(BEST))

    if count != 0:
        main()


def down():
    global field_new
    global SCORE
    global BEST
    count = 0
    for i in range(4):
        for k in range(4):
            for j in range(3, -1, -1):
                if field_new[j][i] != 0 and j != 3:
                    if field_new[j + 1][i] == 0:
                        field_new[j + 1][i] = field_new[j][i]
                        field_new[j][i] = 0
                        count += 1
                    elif field_new[j + 1][i] == field_new[j][i]:
                        field_new[j + 1][i] = field_new[j][i] * 2
                        field_new[j][i] = 0

                        SCORE = SCORE + field_new[j + 1][i] * 10
                        lbl['text'] = ("SCORE\n" + str(SCORE))
                        count += 1

    if BEST < SCORE:
        BEST = SCORE
        lbl2['text'] = ("BEST\n" + str(BEST))

    if count != 0:
        main()


def left():
    global field_new
    global SCORE
    global BEST
    count = 0
    for j in range(4):
        for k in range(4):
            for i in range(4):
                if field_new[j][i] != 0 and i != 0:
                    if field_new[j][i - 1] == 0:
                        field_new[j][i - 1] = field_new[j][i]
                        field_new[j][i] = 0
                        count += 1

                    elif field_new[j][i - 1] == field_new[j][i]:
                        field_new[j][i - 1] = field_new[j][i] * 2
                        field_new[j][i] = 0

                        SCORE = SCORE + field_new[j][i - 1] * 10
                        lbl['text'] = ("SCORE\n" + str(SCORE))
                        count += 1

    if BEST < SCORE:
        BEST = SCORE
        lbl2['text'] = ("BEST\n" + str(BEST))

    if count != 0:
        main()


def right():
    global field_new
    global SCORE
    global BEST
    count = 0
    for j in range(4):
        for k in range(4):
            for i in range(3, -1, -1):
                if field_new[j][i] != 0 and i != 3:
                    if field_new[j][i + 1] == 0:
                        field_new[j][i + 1] = field_new[j][i]
                        field_new[j][i] = 0
                        count += 1
                    elif field_new[j][i + 1] == field_new[j][i]:
                        field_new[j][i + 1] = field_new[j][i] * 2
                        field_new[j][i] = 0

                        SCORE = SCORE + field_new[j][i + 1] * 10
                        lbl['text'] = ("SCORE\n" + str(SCORE))
                        count += 1

    if BEST < SCORE:
        BEST = SCORE
        lbl2['text'] = ("BEST\n" + str(BEST))

    if count != 0:
        main()


def restart():
    global field_new
    global SCORE
    SCORE = 0
    lbl['text'] = ("SCORE\n" + str(SCORE))
    field_new = [[0 for i in range(line)] for j in range(line)]
    check(field_new)
    main()


# КНОПКИ
button_up = Button(root, text='ВВЕРХ', command=up).place(x=size // 2, y=515)
button_down = Button(root, text='ВНИЗ', command=down).place(x=size // 2 + 1, y=545)
button_left = Button(root, text='ВЛЕВО', command=left).place(x=size // 2 - 60, y=545)
button_right = Button(root, text='ВПРАВО', command=right).place(x=size // 2 + 57, y=545)
button_restart = Button(root, text='@', command=restart).place(x=size - 12, y=72)


def check(field_new):
    for y in range(4):
        for x in range(4):
            if field_new[y][x] == 0:
                c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill="#B4B4B4", outline="#7B7B7B", width=5,
                                   tag="2048")

            elif field_new[y][x] == 2:
                c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill="#F1ECD7", outline="#7B7B7B", width=5,
                                   tag="2048")
                c.create_text(x * a + 50, y * a + 50, text=str(field_new[y][x]), fill='#515151', font=('impact', 35),
                              tag="2048")

            elif field_new[y][x] == 4:
                c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill="#FFF1B7", outline="#7B7B7B", width=5,
                                   tag="2048")
                c.create_text(x * a + 50, y * a + 50, text=str(field_new[y][x]), fill='#515151', font=('impact', 35),
                              tag="2048")

            elif field_new[y][x] == 8:
                c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill="#FFBD5F", outline="#7B7B7B", width=5,
                                   tag="2048")
                c.create_text(x * a + 50, y * a + 50, text=str(field_new[y][x]), fill='#F5F5F5', font=('impact', 35),
                              tag="2048")

            elif field_new[y][x] == 16:
                c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill="#FFA92F", outline="#7B7B7B", width=5,
                                   tag="2048")
                c.create_text(x * a + 50, y * a + 50, text=str(field_new[y][x]), fill='#F5F5F5', font=('impact', 35),
                              tag="2048")

            elif field_new[y][x] == 32:
                c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill="#FF752F", outline="#7B7B7B", width=5,
                                   tag="2048")
                c.create_text(x * a + 50, y * a + 50, text=str(field_new[y][x]), fill='#F5F5F5', font=('impact', 35),
                              tag="2048")

            elif field_new[y][x] == 64:
                c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill="#FF3D2F", outline="#7B7B7B", width=5,
                                   tag="2048")
                c.create_text(x * a + 50, y * a + 50, text=str(field_new[y][x]), fill='#F5F5F5', font=('impact', 35),
                              tag="2048")

            elif field_new[y][x] >= 128:
                c.create_rectangle(x * a, y * a, (x + 1) * a, (y + 1) * a, fill="#E5D201", outline="#7B7B7B", width=5,
                                   tag="2048")
                c.create_text(x * a + 50, y * a + 50, text=str(field_new[y][x]), fill='#F5F5F5', font=('impact', 35),
                              tag="2048")


def main():
    global field_new

    # ЗАПИСЬ ВСЕХ СВОБОДНЫХ КЛЕТОК
    nums = []
    for i in range(4):
        for j in range(4):
            if field_new[i][j] == 0:
                nums.append([i, j])
    # РАНДОМНЫЙ ВЫБОР ИЗ НИХ + РАНД ГЕНЕРАЦИЯ 2 & 4
    for i in range(random.randint(1, 2)):
        r = random.randint(0, len(nums) - 1)
        y = nums[r][0]
        x = nums[r][1]
        twofour = [2, 4, 2]
        field_new[y][x] = twofour[random.randint(0, 2)]

    check(field_new)

    c.create_line(0, 3, size, 3, fill="#7B7B7B", width=5)  # Крайние линии не дорисовались
    c.create_line(3, 0, 3, size, fill="#7B7B7B", width=5)  # Ну вот я их и добавил

    root.update()


main()

root.mainloop()
