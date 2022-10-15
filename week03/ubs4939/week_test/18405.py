import heapq
import sys


def find(list_):
    global time
    while time > 0 and list_:
        copy_list = list_.copy()
        list_ = []
        time -= 1
        while copy_list:

            heappop = heapq.heappop(copy_list)

            direction_x = [1, -1, 0, 0]
            direction_y = [0, 0, 1, -1]

            for i in range(4):
                change_x = direction_x[i] + heappop[2]
                change_y = direction_y[i] + heappop[1]

                if change_x < 0 or change_y < 0 or change_x >= size or change_y >= size:
                    continue

                if map_list[change_y][change_x] == 0:
                    map_list[change_y][change_x] = heappop[0]
                    heapq.heappush(list_,(heappop[0],change_y,change_x))


if __name__ == '__main__':
    size, virus_count = map(int, sys.stdin.readline().rstrip().split(" "))

    map_list = []
    for i in range(size):
        map_list.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

    virus_list = []
    time, target_y, target_x = map(int, sys.stdin.readline().rstrip().split(" "))

    for y in range(size):
        for x in range(size):
            if map_list[y][x] != 0:
                heapq.heappush(virus_list, (map_list[y][x], y, x))

    find(virus_list)
    print(map_list[target_y-1][target_x-1])
