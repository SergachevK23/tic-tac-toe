def welcome():
    print('')
    print('Добро пожаловь в игру!!!')
    print('КРЕСТИКИ и НОЛИКИ')
    print('x - строка, y - столбец')

def display():# выводит поле на экран
    print()
    print(f' | 0 | 1 | 2 |')
    print(f'______________')
    for i in range(3):
        print(f"{i}| {meadow[i][0]}  | {meadow[i][1]}  | {meadow[i][2]}  |")
        print(f'______________')

def request():# Ввод пользователя
    while True:
        x, y = map(int, input("   \nваш ход:").split())
        if 0 <= x <= 2 and 0 <= y <= 2:
            if meadow[x][y] == '':
                return x, y
            else:
                print('Клетка занята!')
        else:
            print('Координаты не в диапазона!')

def winning():# проверка выигрышных комбинаций
    win_com = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]

    for com in win_com:
        a = com[0]
        b = com[1]
        c = com[2]
        if meadow[a[0]][a[1]] == meadow[b[0]][b[1]] == meadow[c[0]][c[1]] != "":
            print(f'Выиграл {meadow[a[0]][a[1]]}')
            return True
    return False


num=0
welcome()
meadow = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
while True: # Ход крестика и нолика последовательность
    num += 1

    display()

    if num % 2 == 1:
        print('Ходит X')
    else:
        print('Ходит 0 ')

    x, y = request()

    if num % 2 == 1:
        meadow[x][y] = 'X'
    else:
        meadow[x][y] = 'O'

    if winning():
        break

    if num == 9:
        print('Ничья')
        break


