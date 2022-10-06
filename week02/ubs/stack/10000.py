import collections
import heapq
import sys

if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())
    circle_list = []

    for i in range(count):
        point, length = (map(int, sys.stdin.readline().rstrip().split(" ")))
        circle_list.append((point - length, "B", 2 * length))
        circle_list.append((point + length, "A", -2 * length))

    circle_list.sort(key=lambda x:( x[0], x[1], -x[2]))

    circle_count = 1
    inner = 0

    temp_circle_list = []

    while circle_list:
        circle_pop = circle_list.pop()
        total_sum = 0

        if circle_pop[1] == "A":
            inner += 1
        elif circle_pop[1] == "B":
            circle_count += 1
            while temp_circle_list and -temp_circle_list[0][0] >= inner:
                pop_= heapq.heappop(temp_circle_list)
                if -pop_[0] == inner:
                    total_sum += pop_[1]
            if total_sum == circle_pop[2]:
                circle_count += 1
            inner -= 1
            heapq.heappush(temp_circle_list, (-inner, circle_pop[2]))

    print(circle_count)

    # for i in range(count):
    #     point, length = (map(int, sys.stdin.readline().rstrip().split(" ")))
    #     circle_list.append((point - length, point + length))
    # circle_list.sort(key=lambda x: x[0])
    #
    # print(circle_list)

    # circle_count = 2
    # pop_circle = circle_list.pop()
    # end_list = [pop_circle[1]]
    # while circle_list:
    #     pop_circle = circle_list.pop()
    #
    #     start = pop_circle[0]
    #     end = pop_circle[1]
    #
    #     if len(end_list) > 0:
    #
    #         if end_list[0] < start:
    #             while end_list[0] > start:
    #                 heapq.heappop(end_list)
    #             heapq.heappush(end_list, end)
    #         elif end_list[0] > start:
    #             heapq.heappush(end_list, end)
    #
    #         if len(end_list) > 1:
    #             end_pop = heapq.heappop(end_list)
    #             if end_pop == start and end_list[0] == end:
    #                 circle_count += 1
    #
    #             heapq.heappush(end_list, end_pop)
    #
    #     circle_count += 1
    #
    # print(circle_count)
