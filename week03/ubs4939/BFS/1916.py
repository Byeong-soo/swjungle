import collections
import heapq
import sys


def search_min_price(start, end_point):
    heapq_city = []
    heapq.heappush(heapq_city, (0, start))
    min_price[start] = 0

    while heapq_city:

        pop_city = heapq.heappop(heapq_city)
        visited_list[pop_city[1]] = True

        for city in list_city_price[pop_city[1]]:
            city_number = city[1]
            city_price = city[0]
            min_price[city_number] = min(city_price + min_price[pop_city[1]], min_price[city_number])
            if not visited_list[city_number]:
                heapq.heappush(heapq_city, (min_price[city_number], city_number))
                visited_list[city_number] = True

    print(min_price[end_point])


if __name__ == '__main__':
    city_count = int(sys.stdin.readline().rstrip())
    bus_count = int(sys.stdin.readline().rstrip())
    visited_list = [False for x in range(city_count + 1)]
    min_price = [float('inf') for x in range(city_count + 1)]
    list_city_price = [[] for x in range(city_count + 1)]

    for x in range(bus_count):
        start, end, price = map(int, sys.stdin.readline().rstrip().split(" "))
        heapq.heappush(list_city_price[start], (price, end))

    start_city, end_city = map(int, sys.stdin.readline().rstrip().split(" "))
    search_min_price(start_city, end_city)
