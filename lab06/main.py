import sysv_ipc
import time

game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]


def check():
    for y in game:
        if y == ["X", "X", "X"] or y == ["O", "O", "O"]:
            return 1

    for x in range(3):
        if game[0][x] == game[1][x] == game[2][x] and game[0][x] != " ":
            return 1

    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != " ":
        return 1

    if game[0][2] == game[1][1] == game[2][0] and game[0][2] != " ":
        return 1

    return 0


def make_move(position: (int, int), player: str) -> int:
    if game[position[0]][position[1]] == " ":
        game[position[0]][position[1]] = player
        return 1
    else:
        return 0


def get_position(move: int) -> (int, int):
    y = move // 3
    x = move - 3 * (move // 3)
    return (y, x)


player = "X"
move_counter = 0

while move_counter < 9:
    print(game)
    move = int(input(f"Player {player}: "))
    position = get_position(move)
    if make_move(position, player):
        if check():
            print(f"Player {player} won!")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"
        move_counter += 1

if move_counter >= 9:
    print("Draw")
