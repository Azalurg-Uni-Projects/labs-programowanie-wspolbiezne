# Create a maze of length x in a y by y array

import random


# todo: add a way to validate the x and y values
def neighbors_amount(maze, x, y):
    amount = 0
    if maze[x - 1][y] == 1:
        amount += 1
    if maze[x + 1][y] == 1:
        amount += 1
    if maze[x][y - 1] == 1:
        amount += 1
    if maze[x][y + 1] == 1:
        amount += 1
    return amount


def create_maze(paths: int, size: int):
    if size ** 2 // 2 < paths:
        raise ValueError('Too many paths')

    maze = [[0 for i in range(size)] for j in range(size)]

    x_start = random.randint(0, size - 1)
    y_start = random.randint(0, size - 1)
    if random.random() < 0.5:
        x_start = random.choice([0, size - 1])
    else:
        y_start = random.choice([0, size - 1])

    maze[x_start][y_start] = 1
    occupied = [(x_start, y_start)]
    possible = set()
    while len(occupied) < paths:
        oc = occupied[-1]
        if oc[0] > 1:
            possible.add((oc[0] - 1, oc[1]))
        if oc[0] < size - 2:
            possible.add((oc[0] + 1, oc[1]))
        if oc[1] > 1:
            possible.add((oc[0], oc[1] - 1))
        if oc[1] < size - 2:
            possible.add((oc[0], oc[1] + 1))

        possible = possible - set(occupied)
        chosen = random.choice(list(possible))
        while True:
            if neighbors_amount(maze, chosen[0], chosen[1]) > 1:
                possible.remove(chosen)
                chosen = random.choice(list(possible))
            else:
                break

        occupied.append(chosen)
        maze[chosen[0]][chosen[1]] = 1
        possible.remove(chosen)
    return maze


def print_maze(maze):
    for i in maze:
        for j in i:
            print(j, end='  ')
        print()


def main():
    maze = create_maze(30, 10)
    print_maze(maze)


if __name__ == "__main__":
    main()
