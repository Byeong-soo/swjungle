import heapq
import sys

if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())

    num_list = [int(sys.stdin.readline().rstrip()) for x in range(count)]

    heapq.heapify(num_list)
    total_sum = 0

    if count == 1:
        print(0)
        quit()

    while len(num_list) > 1:

        num1 = heapq.heappop(num_list)
        num2 = heapq.heappop(num_list)

        total_sum += num1
        total_sum += num2

        heapq.heappush(num_list,num1 + num2)

    print(total_sum)
    # while temp_num < count:
    #
    #     if count == 1:
    #         break
    #
    #     if count - temp_num >= 4:
    #         if num_list[0] == num_list[1] == num_list[2] == num_list[3]:
    #
    #             if temp_num == 0:
    #                 total_sum +=first_num
    #
    #             total_sum += num_list[temp_num] * 8
    #             temp_num += 4
    #
    #             continue
    #     pop_number = heapq.heappop(num_list)
    #     total_sum += pop_number * (count - temp_num)
    #
    #     temp_num += 1
    #
    # if count == 1:
    #     print(num_list[0])
    # else:
    #     print(total_sum -first_num)
