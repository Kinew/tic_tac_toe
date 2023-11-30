# Игра Крестики- нолики

# Количество клеток
board_size = 3

# Игровое поле
board = [1,2,3,4,5,6,7,8,9]

def draw_board():
    '''Выводим игровое поле'''
    print("_" * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|')*3)
        print('',board[i * 3], '|',board[1 + i * 3], '|',board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)

def game_step(index, char):
    '''Выполняем ход'''
    if (index > 10 or index < 1 or board[index - 1] in ('x','o')):
        return False

    board[index - 1] = char
    return True

def chek_win():
    '''Проверяем победу одного из игроков'''
    win = False

    win_combination = (
        (0,1,2), (3,4,5), (6,7,8),   # горизонтальные линии
        (0,3,6), (1,4,7), (2,5,8),   # вертикальные линии
        (0,4,8), (2,4,6)            # диагональные линии
    )

    for pos in win_combination:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]

    return win

def start_game():
    # текущий игрок
    current_player = 'x'
    # номер шага
    step = 1
    draw_board()

    while(step < 9) and (chek_win() == False):
        index = input("Ходит игрок " + current_player + ". Введите номер поля (0 - Выход:")

        if (int(index) == '0'):
            break
          # Если получилось сделать ход
        if (game_step(int(index), current_player)):
            print("Удачный ход ")

            if (current_player == 'x'):
                current_player = '0'
            else:
                current_player = 'x'

            draw_board()
            # увеличим номер хода
            step += 1
        else:
            print("Неверный номер, повторите!")

    if (step == 9):
        print("Игра окончена, ничья")
    else:
        print("Выиграл" + chek_win())

        # game_step(int(index), current_player)

print("Добро пожаловать в игру крестики- нолики")
start_game()