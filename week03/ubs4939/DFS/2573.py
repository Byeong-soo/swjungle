import heapq
import sys

sys.setrecursionlimit(10**7)

def find_first_glacier():
    for row in range(1, height):
        start = 1
        end = width - 2

        while start <= end:
            if map_list[row][start] != 0:
                position = (row, start)
                return position

            if map_list[row][end] != 0:
                position = (row, end)
                return position

            start += 1
            end -= 1


def check_around(row, col):
    mount = map_list[row][col]
    see_count = 0
    around = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited_list[row][col] = True
    for val in around:
        if height <= (row + val[0]) < 0 or width <= col + val[1] < 0:
            continue
        if map_list[row + val[0]][col + val[1]] == 0:
            see_count += 1
        else:
            if not visited_list[row + val[0]][col + val[1]]:
                check_around(row + val[0], col + val[1])

    heapq.heappush(glacier_list, (-mount, see_count, row, col))


def melt():
    global time
    alive = 0
    for glacier in glacier_list:
        if (-glacier[0]) - glacier[1] <= 0:
            map_list[glacier[2]][glacier[3]] = 0
        else:
            map_list[glacier[2]][glacier[3]] = (-glacier[0]) - glacier[1]
            alive += 1
    time += 1
    return alive


if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().rstrip().split(" "))

    map_list = []
    glacier_list = []

    for _ in range(height):
        map_list.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

    time = 0
    start = 0
    all_melt = False
    end = width
    first_glacier = find_first_glacier()
    visited_list = [[False for x in range(width)] for y in range(height)]
    check_around(first_glacier[0], first_glacier[1])

    if len(glacier_list) <= 1:
        print(0)
        exit()

    while glacier_list:
        # 멜트해서 남은 갯수랑
        alive = melt()

        if alive <= 1:
            all_melt = True
            break

        pop_glacier = heapq.heappop(glacier_list)
        glacier_list = []
        visited_list = [[False for x in range(width)] for y in range(height)]
        # DFS한 결과가 같아야함
        check_around(pop_glacier[2], pop_glacier[3])

        if alive != len(glacier_list):
            break

    if all_melt:
        print(0)
    else:
        print(time)