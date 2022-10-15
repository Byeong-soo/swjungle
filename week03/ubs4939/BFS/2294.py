import collections
import sys


if __name__ == '__main__':
    kind, target = map(int, sys.stdin.readline().rstrip().split(" "))

    visited_list = [False for x in range(10001)]
    min_way = [float('inf') for x in range(10001)]

    coin_set = set([])
    for count in range(kind):
        coin_set.add(int(sys.stdin.readline().rstrip()))

    coin_list = list(coin_set)

    min_way[0] = 0

    for coin in coin_list:
        for x in range(coin,target+1):
            min_way[x] = min(min_way[x],min_way[x-coin] + 1)
    if min_way[target] == float('inf'):
        print(-1)
    else:
        print(min_way[target])



