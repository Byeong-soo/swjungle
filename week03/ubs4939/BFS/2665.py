import heapq
import sys


def search(start_point):
    direction_x = [1, -1, 0, 0]
    direction_y = [0, 0, 1, -1]
    heapq_position = []
    visited_list[start_point[1]][start_point[2]] = True
    weight_list[start_point[1]][start_point[2]] = 0

    heapq.heappush(heapq_position, start_point)

    while heapq_position:

        pop_position = heapq.heappop(heapq_position)

        for i in range(4):
            change_x = pop_position[1] + direction_x[i]
            change_y = pop_position[2] + direction_y[i]

            if change_x < 0 or change_x >= room_size or change_y < 0 or change_y >= room_size:
                continue

            if not visited_list[change_x][change_y]:
                visited_list[change_x][change_y] = True

                pop_position_weight = weight_list[pop_position[1]][pop_position[2]]
                new_position_weight = weight_list[change_x][change_y]

                if room_list[change_x][change_y] == 1:
                    weight_list[change_x][change_y] = min(pop_position_weight, new_position_weight)
                    heapq.heappush(heapq_position, (weight_list[change_x][change_y],change_x,change_y))
                elif room_list[change_x][change_y] == 0:
                    weight_list[change_x][change_y] = min(pop_position_weight +1, new_position_weight)
                    heapq.heappush(heapq_position, (weight_list[change_x][change_y],change_x,change_y))


if __name__ == '__main__':
    room_size = int(sys.stdin.readline().rstrip())

    room_list = [list(map(int, list(sys.stdin.readline().rstrip()))) for x in range(room_size)]
    visited_list = [[False for x in range(room_size)] for y in range(room_size)]
    weight_list = [[2500 for x in range(room_size)] for y in range(room_size)]
    start = (0, 0, 0)
    search(start)

    print(weight_list[room_size-1][room_size-1])

