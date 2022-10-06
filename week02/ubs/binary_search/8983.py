import heapq
import sys

if __name__ == '__main__':
    gun_count, animal_count, gun_range = map(int, sys.stdin.readline().rstrip().split(" "))

    gun_position_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    gun_position_list.sort()

    animal_position_list = []

    for count in range(animal_count):
        x, y = map(int, sys.stdin.readline().rstrip().split(" "))
        if y > gun_range:
            continue
        animal_position_list.append((x, y))

    kill_count = 0
    temp = []

    start = 0
    end = gun_count - 1
    global mid_gun

    for animal_position in animal_position_list:
        start = 0
        end = gun_count - 1
        min_value = 1000000000000
        shot_gun = 0
        while start <= end:
            mid_gun = (start + end) // 2

            value = abs(gun_position_list[mid_gun] - animal_position[0])
            if min_value >= value:
                min_value = value
                shot_gun = mid_gun

            if gun_position_list[mid_gun] - animal_position[0] > 0:
                end = mid_gun -1
            elif gun_position_list[mid_gun] - animal_position[0] < 0:
                start = mid_gun + 1
            else:
                break

        if abs(gun_position_list[shot_gun] - animal_position[0]) + animal_position[1] <= gun_range:
            kill_count += 1

    print(kill_count)
