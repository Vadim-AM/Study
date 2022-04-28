outcomes = ["X wins", "O wins", "Draw", "Game not finished", "Impossible"]
matrix = [['_'] * 3 for _ in range(3)]  # создание матрицы через строчный ввод


def x_wins(mx):
    diagonal1, diagonal2 = '', ''
    vertical1, s = '', ''
    for i in range(3):
        if s.join(mx[i]) == 'XXX':  # проверка горизонтали
            return 0
        for j in mx:
            vertical1 += j[i]
        if vertical1 == 'XXX':
            return 0
        for j in range(3):
            if i == j:  # проверка основной диагонали
                diagonal1 += mx[i][j]
            if i + j + 1 == 3:  # проверка второстепенной диагонали
                diagonal2 += mx[i][j]
            if diagonal1 == 'XXX' or diagonal2 == 'XXX':
                return 0
        vertical1 = ''


def o_wins(mx):
    diagonal1, diagonal2 = '', ''
    vertical1, s = '', ''
    for i in range(3):
        if s.join(mx[i]) == 'OOO':  # проверка горизонтали
            return 1
        for j in mx:
            vertical1 += j[i]
        if vertical1 == 'OOO':
            return 1
        for j in range(3):
            if i == j:  # проверка основной диагонали
                diagonal1 += mx[i][j]
            if i + j + 1 == 3:  # проверка второстепенной диагонали
                diagonal2 += mx[i][j]
            if diagonal1 == 'OOO' or diagonal2 == 'OOO':
                return 1
        vertical1 = ''


def drawing(mx):  # отрисовка игрового поля построчно
    print('-' * 9)
    for i in range(3):
        print('|', *mx[i], '|')
    print('-' * 9)


def impossible(mx, arg1, arg2, counter):
    if arg1 == 0 and arg2 == 1:  # принимает возврат победы по Х,О
        return 4
    _, x, zero = 0, 0, 0
    for i in mx:
        for j in i:
            if j == 'X':
                x += 1
            elif j == 'O':
                zero += 1
            elif j == '_':
                _ += 1
    if _ == 0 and (arg1 != 0 and arg2 != 1):  # проверка ничья
        return 2
    elif abs(x - zero) > 2:  # сравнение количества Х и О на невозможность
        return 4
    elif _ != 0 and (arg1 != 0 and arg2 != 1):  # проверка окончания игры
        return 3


def game_check(x_win, o_win, impossibl, counter):  # итоговая проверка адекватности поля
    if x_win == 0:
        return print(outcomes[0])
    elif o_win == 1:
        return print(outcomes[1])
    elif impossibl == 2:
        return print(outcomes[2])
    elif impossibl == 4:
        return print(outcomes[4])
    else:
        user_input(counter)


def replacing_cell(mx, i: int, j: int, counter):  # проверка клеток и отрисовка матрицы в случае позитивного сценария
    if 3 > i >= 0 and 3 > j >= 0:
        if mx[i][j] != '_':
            print('This cell is occupied! Choose another one!')
            user_input(counter)
        elif counter % 2 == 0:  # Выбор символа
            mx[i][j] = 'X'
            counter += 1
        elif counter % 2 != 0:
            mx[i][j] = 'O'
            counter += 1
        drawing(mx)
        game_check(x_wins(matrix), o_wins(matrix), impossible(matrix, x_wins(matrix), o_wins(matrix), counter), counter)
    else:
        print('Coordinates should be from 1 to 3!')
        user_input(counter)


def user_input(counter):  # пропускает только цифры по типу введенных данных
    try:
        x, y = (int(i) for i in input('Enter the coordinates:').split())
    except ValueError:
        print('You should enter numbers!')
        user_input(counter)
    else:
        replacing_cell(matrix, x - 1, y - 1, counter)  # смещает на единицу ввод ибо range считается с 0!


drawing(matrix)
user_input(counter=0)
