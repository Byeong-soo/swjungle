import collections
import sys


def find_home(start):
    global house_number
    direction_x = [1, -1, 0, 0]
    direction_y = [0, 0, 1, -1]

    deque = collections.deque([start])
    house_number = 0
    visited_list[start[0]][start[1]] = True

    if map_list[start[0]][start[1]] == 1:
        house_number+=1

    while deque:

        pop = deque.popleft()

        for i in range(4):
            change_x = pop[1] + direction_x[i]
            change_y = pop[0] + direction_y[i]

            if change_x < 0 or change_y < 0 or change_y >= size or change_x >= size:
                continue

            if not visited_list[change_y][change_x]:
                visited_list[change_y][change_x] = True

                if map_list[change_y][change_x] == 0:
                    continue
                if map_list[change_y][change_x] == 1:
                    deque.append((change_y, change_x))
                    house_number += 1

    if house_number != 0:
        home_number_list.append(house_number)


if __name__ == '__main__':
    size = int(sys.stdin.readline().rstrip())

    house_number = 0
    map_list = []
    visited_list = [[False for x in range(size)] for y in range(size)]
    home_number_list = []

    for x in range(size):
        map_list.append(list(map(int, list(sys.stdin.readline().rstrip()))))

    start_position = (0, 0)

    for y in range(size):
        for x in range(size):
            if not visited_list[y][x]:
                find_home((y, x))

    home_number_list.sort()
    print(len(home_number_list))
    for home_number in home_number_list:
        print(home_number)

