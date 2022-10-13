import collections
import heapq
import sys


def bfs(start):
    list_ = []
    heapq.heappush(list_, start)
    visited[start[1]] = True
    price_list[start[1]] = 0

    while list_:
        pop = heapq.heappop(list_)

        for city in city_list[pop[1]]:
            price_list[city[1]] = min(price_list[city[1]], price_list[pop[1]] + city[0])
            if not visited[city[1]]:
                heapq.heappush(list_, (price_list[city[1]], city[1]))
                visited[city[1]] = True


if __name__ == '__main__':
    city_count = int(sys.stdin.readline().rstrip())
    bus_count = int(sys.stdin.readline().rstrip())
    price_list = [float('inf') for x in range(city_count + 1)]
    visited = [False for x in range(city_count + 1)]



    city_list = [[] for x in range(city_count + 1)]

    for x in range(bus_count):
        start, end, price = map(int, sys.stdin.readline().rstrip().split(" "))
        heapq.heappush(city_list[start], (price, end))

    start_point, target = map(int, sys.stdin.readline().rstrip().split(" "))
    bfs((0, start_point))

    print(price_list[target])
