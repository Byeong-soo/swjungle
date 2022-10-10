import collections
import sys

if __name__ == '__main__':
    y, x = map(int, sys.stdin.readline().rstrip().split(" "))
    global home_position
    global find_check

    map_list = []

    for _ in range(y):
        map_list.append(list(sys.stdin.readline().rstrip()))

    home_position = (0, 0)
    start_position = (0, 0)
    time = 0
    find_check = False

    start_list = []
    water_list = []

    for row in range(y):
        for col in range(x):
            if map_list[row][col] == "D":
                home_position = (row, col)
            elif map_list[row][col] == "S":
                start_position = (row, col)
                start_list.append((row, col))
            elif map_list[row][col] == "*":
                water_list.append((row, col))

    day_water_list = collections.deque([])
    day_start_list = collections.deque([])

    day_water_list.append(water_list)
    day_start_list.append(start_list)

    while day_start_list:

        start_list = []
        pop_start_list = day_start_list.popleft()

        direction_x = [1, -1, 0, 0]
        direction_y = [0, 0, 1, -1]

        if day_water_list:

            water_list = []
            pop_water_list = day_water_list.popleft()

            for water in pop_water_list:

                for i in range(4):
                    change_y = water[0] + direction_y[i]
                    change_x = water[1] + direction_x[i]

                    if x > change_x >= 0 and y > change_y >= 0 and (map_list[change_y][change_x] == "." or \
                            map_list[change_y][change_x] == "S"):
                        map_list[change_y][change_x] = "*"
                        water_list.append((change_y, change_x))
            if water_list:
                day_water_list.append(water_list)

        for start in pop_start_list:
            for i in range(4):
                change_y = start[0] + direction_y[i]
                change_x = start[1] + direction_x[i]

                if x > change_x >= 0 and y > change_y >= 0 and (map_list[change_y][change_x] == "." or map_list[change_y][change_x] == "D"):
                    map_list[change_y][change_x] = "S"
                    start_list.append((change_y, change_x))
                    start_position = (change_y, change_x)
                    if start_position == home_position:
                        find_check = True
                        break

        if start_list:
            day_start_list.append(start_list)

        time += 1

        if find_check:
            break

    if find_check:
        print(time)
    else:
        print("KAKTUS")
