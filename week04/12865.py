import heapq
import sys

if __name__ == '__main__':
    good_count, bag_weight = map(int, sys.stdin.readline().rstrip().split(" "))
    max_weight_list = [0 for x in range(bag_weight + 1)]

    good_list = []
    for _ in range(good_count):
        good_weight, good_price = map(int, sys.stdin.readline().rstrip().split(" "))
        good_list.append((good_weight, good_price))

    for good in good_list:
        weight, price = good

        for x in range(bag_weight, weight - 1, -1):
            max_weight_list[x] = max(max_weight_list[x], max_weight_list[x - weight] + price)

    print(max_weight_list[-1])

    # 삽질
    #     heapq.heappush(weight_list, (good_weight, good_price))
    #
    # for _ in range(len(weight_list)):
    #     heappop = heapq.heappop(weight_list)
    #
    #     good_price = heappop[1]
    #     good_weight = heappop[0]
    #
    #     max_weight_list[good_weight] = max(good_price, max_weight_list[good_weight])
    #
    #     if 2 * good_weight <= weight:
    #
    #         if good_price >= max_weight_list[good_weight]:
    #
    #             for x in range(good_weight + 1, 2 * good_weight):
    #                 max_weight_list[x] = max(max_weight_list[x], max_weight_list[x - good_weight] + good_price)
    #             for x in range(2 * good_weight, weight + 1):
    #                 max_weight_list[x] = max(max_weight_list[x], max_weight_list[x - 1])
    #         else:
    #             for x in range(good_weight + 1, 2 * good_weight+1):
    #                 max_weight_list[x] = max(max_weight_list[x], max_weight_list[x - good_weight] + good_price)
    #             for x in range(2 * good_weight + 1, weight + 1):
    #                 max_weight_list[x] = max(max_weight_list[x], max_weight_list[x - 1])
    #
    #     else:
    #         for x in range(good_weight + 1, weight + 1):
    #             max_weight_list[x] = max(max_weight_list[x], max_weight_list[x - good_weight] + good_price)
    #
    # print(max_weight_list[weight])
