''' 
Задача №40: 
Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.
Игра начинается с хода человека, который ставит крестики
'''

import random
from tkinter import *

root = Tk()         # делаем окно с заголовком
root.title('Крестики-нолики')

game_run = True     # если будет победитель, будет False
field = []          # в массиве храним состояние поля
cross_count = 0     # Подсчитываем количество крестиков на поле, максимально 5


def new_game():     # поле и переменные обнуляются
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):        # ставим крестик и считаем
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')      # проверка на победу
        if game_run and cross_count < 5:
            computer_move()
            check_win('O')  # проверка на победу

# проверка победы по всем направлениям


def check_win(smb):
    for n in range(3):
        check_line(field[n][0], field[n][1], field[n][2], smb)
        check_line(field[0][n], field[1][n], field[2][n], smb)
    check_line(field[0][0], field[1][1], field[2][2], smb)
    check_line(field[2][0], field[1][1], field[0][2], smb)

# на входе три поля и символ, если символ есть в этих трех полях,
# то меняем цвет полей на розовый и остановка игры


def check_line(a1, a2, a3, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = 'pink'
        global game_run
        game_run = False


def can_win(a1, a2, a3, smb):   # проверка на победу
    res = False
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
        a1['text'] = 'O'
        res = True
    return res


def computer_move():
    for n in range(3):
        if can_win(field[n][0], field[n][1], field[n][2], 'O'):
            return
        if can_win(field[0][n], field[1][n], field[2][n], 'O'):
            return
    if can_win(field[0][0], field[1][1], field[2][2], 'O'):
        return
    if can_win(field[2][0], field[1][1], field[0][2], 'O'):
        return

    while True:  # случ. образом перебираются поля, пока не выпадет свободное
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break


for row in range(3):  # создаем поле кнопок
    line = []
    for col in range(3):
        button = Button(text=' ', width=6, height=3,
                        font=('Verdana', 22, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)

new_button = Button(text='Новая игра', command=new_game)
new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')

root.mainloop()
