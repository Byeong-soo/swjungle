import heapq
import sys

if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())
    list_ = []
    for i in range(count):
        start, end = map(int, sys.stdin.readline().rstrip().split(" "))
        heapq.heappush(list_, (end, start))

    num = 0
    end_time = 0
    while list_:
        heappop = heapq.heappop(list_)
        print(heappop)
        if heappop[1] >= end_time:
            num += 1
            end_time = heappop[0]
    print(num)


