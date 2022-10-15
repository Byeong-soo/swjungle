import collections
import sys

if __name__ == '__main__':
    width, height, vertical = map(int, sys.stdin.readline().rstrip().split(" "))
    count = height * vertical

    tomato_box = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for x in range(count)]

    # 1 = 익은 토마토
    # 0 = 안익은 토마토
    # -1 = 토마토 없음

    good_tomato_list = []
    day = 0
    good_tomato_count = 0
    bad_tomato_count = 0
    empty_count = 0

    for z in range(vertical):
        for y in range(height):
            for x in range(width):
                if tomato_box[y + (height * z)][x] == 1:
                    good_tomato_list.append((z, y, x))
                elif tomato_box[y + (height * z)][x] == 0:
                    bad_tomato_count += 1

    direction_x = [1, -1, 0, 0, 0, 0]
    direction_y = [0, 0, 1, -1, 0, 0]
    direction_z = [0, 0, 0, 0, 1, -1]

    deque_tomato_list = collections.deque([good_tomato_list])

    if len(good_tomato_list) == vertical * height * width:
        print(0)
        exit()

    while deque_tomato_list:
        day_tomato_list = []
        pop_tomato = deque_tomato_list.popleft()

        for tomato in pop_tomato:

            for i in range(6):
                change_z = tomato[0] + direction_z[i]
                change_y = tomato[1] + direction_y[i]
                change_x = tomato[2] + direction_x[i]

                if vertical > change_z >= 0 and 0 <= change_y < height and width > change_x >= 0 == \
                        tomato_box[(change_z * height) + change_y][change_x]:
                    tomato_box[(change_z * height) + change_y][change_x] = 1
                    day_tomato_list.append((change_z, change_y, change_x))
                    bad_tomato_count -= 1

        if day_tomato_list:
            deque_tomato_list.append(day_tomato_list)

        day += 1

    if bad_tomato_count == 0:
        print(day-1)
    else:
        print(-1)
