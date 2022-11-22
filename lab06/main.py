import sysv_ipc
import time

player = "X"
move_counter = 0
game = "         "

key = 12
NULL_CHAR = '\0'

try:
    sem1 = sysv_ipc.Semaphore(key, sysv_ipc.IPC_CREX, 0o700, 0)
    sem2 = sysv_ipc.Semaphore(key + 1, sysv_ipc.IPC_CREX, 0o700, 1)
    mem = sysv_ipc.SharedMemory(key, sysv_ipc.IPC_CREX)
    player = "X"
except sysv_ipc.ExistentialError:
    sem1 = sysv_ipc.Semaphore(key + 1)
    sem2 = sysv_ipc.Semaphore(key)
    mem = sysv_ipc.SharedMemory(key)
    player = "O"
    time.sleep(0.1)


def read_game(mem):
    s = mem.read()
    s = s.decode()
    i = s.find(NULL_CHAR)
    if i != -1:
        s = s[:i]
    return s


def save_game(mem, s):
    s += NULL_CHAR
    s = s.encode()
    mem.write(s)


def print_game():
    for x in range(0, 9, 3):
        print(f" {game[x]} | {game[x + 1]} | {game[x + 2]}")
        if x < 5:
            print("-----------")


def check():
    for y in range(0, 9, 3):
        if game[y] == game[y + 1] == game[y + 2] and game[y] != " ":
            return game[y]

    for x in range(3):
        if game[x] == game[x+3] == game[x+6] and game[x] != " ":
            return game[x]

    if game[0] == game[4] == game[8] and game[4] != " ":
        return game[4]

    if game[2] == game[4] == game[6] and game[4] != " ":
        return game[4]

    return False


def make_move(position: int, player: str, game_coppy: str):
    arr = []
    for x in game_coppy:
        arr.append(x)
    arr[position] = player
    game_coppy = ""
    for x in arr:
        game_coppy += x
    return game_coppy


if player == "X":
    save_game(mem, game)
else:
    move_counter += 1

while move_counter < 5:
    sem2.acquire()
    game = read_game(mem)
    print_game()

    if check():
        print(f"Player {check()} won!")
        break

    move = int(input(f"Player {player}: "))
    position = move - 1

    while True:
        if game[position] == " ":
            game = make_move(position, player, game)
            save_game(mem, game)
            break
        else:
            move = int(input(f"Player {player}: "))
            position = move - 1

    if check():
        print(f"Player {check()} won!")
        sem1.release()
        break

    move_counter += 1
    sem1.release()


if move_counter >= 5:
    print("Draw")

try:
    sysv_ipc.remove_shared_memory(mem.id)
    sysv_ipc.remove_semaphore(sem1.id)
    sysv_ipc.remove_semaphore(sem2.id)
except sysv_ipc.ExistentialError:
    pass
