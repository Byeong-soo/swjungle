import collections
import heapq
import sys


def find_room(start_y, start_x):
    mini[start_y][start_x] = 0
    visited[start_y][start_x] = True

    direction_x = [1, -1, 0, 0]
    direction_y = [0, 0, -1, 1]
    list_ = []
    heapq.heappush(list_,(start_y,start_x))

    while list_:
        pop = heapq.heappop(list_)

        for i in range(4):
            change_x = pop[1] + direction_x[i]
            change_y = pop[0] + direction_y[i]

            if change_x < 0 or change_y < 0 or change_y >= size or change_x >= size:
                continue

            if not visited[change_y][change_x]:

                if room_list[change_y][change_x] == 0:
                    mini[change_y][change_x] = min(mini[change_y][change_x], mini[pop[0]][pop[1]] + 1)
                else:
                    mini[change_y][change_x] = min(mini[change_y][change_x], mini[pop[0]][pop[1]])
                visited[change_y][change_x] = True
                heapq.heappush(list_,(change_y,change_x))


if __name__ == '__main__':
    size = int(sys.stdin.readline().rstrip())
    room_list = []
    mini = [[float('inf') for x in range(size)] for y in range(size)]
    visited = [[False for x in range(size)] for y in range(size)]

    for x in range(size):
        room_list.append(list(map(int, list(sys.stdin.readline().rstrip()))))

    find_room(0,0)
    print(mini[size - 1][size - 1])
