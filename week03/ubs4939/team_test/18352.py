import collections
import sys

def bfs(start):

    deque = collections.deque([start])
    price_list[start] = 0
    visited[start] = True

    while deque:
        pop = deque.popleft()
        for x in city_list[pop]:
            if price_list[x] > price_list[pop] + 1:
                price_list[x] = price_list[pop] + 1
            if not visited[x]:
                deque.append(x)
                visited[x] = True


if __name__ == '__main__':
    city_count, road_count, distance, start_city = map(int, sys.stdin.readline().rstrip().split(" "))

    city_list = [[] for x in range(city_count + 1)]
    price_list = [float('inf') for x in range(city_count + 1)]
    visited = [False for x in range(city_count + 1)]

    for x in range(road_count):
        start, end = map(int,sys.stdin.readline().rstrip().split(" "))
        city_list[start].append(end)

    bfs(start_city)
    check = False
    for i in range(1,len(price_list)):
        if price_list[i] == distance:
            print(i)
            check = True

    if not check:
        print(-1)




