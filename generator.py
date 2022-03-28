import random


def print_maze(board):
    for each in board:
        print(" ".join(each))


def any_unvisited(x, y, rows, cols, visited):
    unv = []
    if x > 0:
        if not visited[y][x - 1]:
            unv.append('left')
    if x < cols - 1:
        if not visited[y][x + 1]:
            unv.append('right')
    if y > 0:
        if not visited[y - 1][x]:
            unv.append('up')
    if y < rows - 1:
        if not visited[y + 1][x]:
            unv.append('down')
    return unv


def generate_maze(size_x, size_y):
    maze = [['#' for _ in range(2 * size_x + 1)] for _ in range(2 * size_y + 1)]
    visited = [[False for _ in range(size_x)] for _ in range(size_y)]
    stack = []
    start_x, start_y = [1, 0]
    visited[start_y][start_x] = True
    maze[start_y][start_x] = '0'
    stack.append((start_y, start_x))
    while stack:
        curr_y, curr_x = stack.pop()
        unvisited = any_unvisited(curr_x, curr_y, size_x, size_y, visited)
        if unvisited:
            stack.append((curr_y, curr_x))
            direction = random.choice(unvisited)
            if direction == 'left':
                adj_x, adj_y = curr_x - 1, curr_y
            elif direction == 'right':
                adj_x, adj_y = curr_x + 1, curr_y
            elif direction == 'up':
                adj_x, adj_y = curr_x, curr_y - 1
            elif direction == 'down':
                adj_x, adj_y = curr_x, curr_y + 1
            stack.append((adj_y, adj_x))
            maze[adj_y * 2 + 1][adj_x * 2 + 1] = ' '
            maze[curr_y * 2 + 1][curr_x * 2 + 1] = ' '
            maze[adj_y + curr_y + 1][adj_x + curr_x + 1] = ' '
            visited[adj_y][adj_x] = True
    print_maze(maze)


generate_maze(10, 10)
