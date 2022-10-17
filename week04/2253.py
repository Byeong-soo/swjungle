import sys

if __name__ == '__main__':
    stone_count, mini_stone_count = map(int, sys.stdin.readline().rstrip().split(" "))

    # mini_list = list(set(map(int,sys.stdin.readline().rstrip().split(" "))))
    #
    # for i in mini_list:
    #     stone_list[i] = -1

    stone = set()
    for _ in range(mini_stone_count):
        stone_number = int(sys.stdin.readline().rstrip())
        stone.add(stone_number)

    speed_val = int((2 * stone_count) ** 0.5) + 1
    stone_dp = [[float('inf') for x in range(speed_val + 1)] for y in range(stone_count + 1)]

    stone_dp[1][0] = 0

    for i in range(2, stone_count + 1):
        if i in stone:
            continue
        for x in range(1, speed_val):
            stone_dp[i][x] = min(stone_dp[i - x][x - 1], stone_dp[i - x][x], stone_dp[i - x][x + 1]) + 1

    answer = min(stone_dp[stone_count])
    if answer == float('inf'):
        print(-1)
    else:
        print(answer)

    # BFS? 방식? 시간초과
    # stone_list = [[0, 0, True] for x in range(stone_count + 1)]
    # for x in range(mini_stone_count):
    #     index = int(sys.stdin.readline().rstrip())
    #     stone_list[index] = [-1, -1, True]
    # check = True
    #
    # position = 1
    # count = 0
    # max_distance = 0
    # while check:
    #     if position == stone_count:
    #         break
    #     check1, check2, check3 = False, False, False
    #     chec = False
    #
    #     if position + max_distance + 1 <= stone_count:
    #         if stone_list[position + max_distance + 1][0] != -1:
    #             stone_list[position + max_distance + 1] = [max_distance + 1, count+1, False]
    #             check1 = True
    #     if position + max_distance <= stone_count and max_distance != 0:
    #         if stone_list[position + max_distance][0] != -1:
    #             stone_list[position + max_distance] = [max_distance, count+1, False]
    #             check2 = True
    #     if max_distance - 1 > 0 and position + max_distance -1 <= stone_count:
    #         if stone_list[position + max_distance - 1][0] != -1:
    #             stone_list[position + max_distance - 1] = [max_distance - 1, count+1, False]
    #             check3 = True
    #
    #     if check1:
    #         stone_list[position + max_distance + 1][2] = True
    #         position += max_distance + 1
    #         max_distance +=1
    #         count += 1
    #     elif check2:
    #         stone_list[position + max_distance][2] = True
    #         position += max_distance
    #         count += 1
    #     elif check3:
    #         stone_list[position + max_distance - 1][2] = True
    #         position += max_distance - 1
    #         max_distance -= 1
    #         count += 1
    #     else:
    #         for stone in range(position - 1, 0, -1):
    #             if not stone_list[stone][2]:
    #                 position = stone
    #                 max_distance = stone_list[stone][0]
    #                 count = stone_list[stone][1]
    #                 chec = True
    #                 break
    #         if not chec:
    #             check = False
    #             break
    # if check:
    #     print(count)
    # else:
    #     print(-1)
