import queue

maze = [
    ['#', '0', '#', '#', '#', '#', '#', '#', '#', '#'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' '],
    [' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#', ' '],
    ['#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' '],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' '],
    ['#', 'X', '#', '#', '#', '#', '#', '#', '#', '#']
]

visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

rows = len(maze[0])
cols = len(maze)
start_x = maze[0].index('0')
start_y = 0
end_x = maze[cols - 1].index('X')
end_y = cols - 1

q = queue.Queue()
q.put((start_y, start_x))

step = 1


def print_maze(maze):
    for row in maze:
        for cell in row:
            cell = cell.ljust(3)
            print(cell, end='')
        print('')


def traverse(y, x):
    if y > 0:
        if maze[y - 1][x] != '#' and not visited[y - 1][x]:
            maze[y - 1][x] = str(step)
            q.put((y - 1, x))
    if y < cols - 1:
        if maze[y + 1][x] != '#' and not visited[y + 1][x]:
            maze[y + 1][x] = str(step)
            q.put((y + 1, x))
    if x > 0:
        if maze[y][x - 1] != '#' and not visited[y][x - 1]:
            maze[y][x - 1] = str(step)
            q.put((y, x - 1))
    if x < rows - 1:
        if maze[y][x + 1] != '#' and not visited[y][x + 1]:
            maze[y][x + 1] = str(step)
            q.put((y, x + 1))


while maze[end_y][end_x] == 'X':
    curr_y, curr_x = q.get()
    step = int(maze[curr_y][curr_x]) + 1
    visited[curr_y][curr_x] = True
    traverse(curr_y, curr_x)

print_maze(maze)
