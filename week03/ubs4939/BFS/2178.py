import collections
import sys


def go_maze(position, height, width):

    position_deque = collections.deque([position])

    while position_deque:

        pop_position = position_deque.popleft()

        for z in range(4):
            y = pop_position[0] + direction_up_down[z]
            x = pop_position[1] + direction_left_right[z]

            if y < 0 or y >= height or x < 0 or x >= width:
                continue

            if maze_list[y][x] == 0:
                continue

            if not visited_list[y][x]:
                position_deque.append((y,x))
                maze_list[y][x] += maze_list[pop_position[0]][pop_position[1]]
                visited_list[y][x] = True



if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().rstrip().split(" "))

    maze_list = []
    visited_list = [[False for y in range(width)] for x in range(height)]
    for x in range(height):
        maze_list.append(list(map(int, list(sys.stdin.readline().rstrip()))))

    position = [0, 0]
    visited_list[0][0] = True
    direction_up_down = [1, -1, 0, 0]
    direction_left_right = [0, 0, -1, 1]

    go_maze((0,0),height,width)
    print(maze_list[height-1][width-1])
