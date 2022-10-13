import collections
import sys


def bfs(start_x, start_y):
    direction_x = [0, 0, -1, 1]
    direction_y = [1, -1, 0, 0]

    deque = collections.deque([(start_y, start_x)])
    visited_list[start_y][start_x] = True

    while deque:

        pop_maze = deque.popleft()

        for i in range(4):
            change_x = direction_x[i] + pop_maze[1]
            change_y = direction_y[i] + pop_maze[0]

            if change_x < 0 or change_x >= width or change_y <0 or change_y >= height:
                continue

            if maze_list[change_y][change_x] == 1:
                if not visited_list[change_y][change_x]:
                    visited_list[change_y][change_x] = True
                    deque.append((change_y, change_x))
                    maze_list[change_y][change_x] = maze_list[pop_maze[0]][pop_maze[1]] + maze_list[change_y][change_x]


if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().rstrip().split(" "))
    visited_list = [[False for x in range(width)] for y in range(height)]
    maze_list = []
    for y in range(height):
        maze_list.append(list(map(int, list(sys.stdin.readline().rstrip()))))

    bfs(0, 0)
    print(maze_list[height - 1][width - 1])
