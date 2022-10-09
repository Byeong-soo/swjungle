import collections
import sys


def check_distance(root, target):
    global result
    result = []
    city_deque = collections.deque([root])
    distance_list[root] = 0
    visited_list[root] = True

    while city_deque:
        pop_city = city_deque.popleft()
        for city in city_list[pop_city]:
            if not visited_list[city]:
                city_deque.append(city)
                distance_list[city] = distance_list[pop_city] + 1
                visited_list[city] = True
                if distance_list[city] == target:
                    result.append(city)


if __name__ == '__main__':
    city_count, road_count, target_distance, start_city = map(int, sys.stdin.readline().rstrip().split(" "))

    city_list = [[] for x in range(city_count + 1)]
    visited_list = [False for x in range(city_count + 1)]
    distance_list = [-1 for x in range(city_count + 1)]

    for _ in range(road_count):
        start, end = map(int, sys.stdin.readline().rstrip().split(" "))
        city_list[start].append(end)

    result = []
    check_distance(start_city, target_distance)

    if result:
        result.sort()
        print(*result,sep="\n")
    else:
        print(-1)
