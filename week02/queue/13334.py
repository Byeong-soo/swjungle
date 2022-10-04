import heapq
import sys

if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())

    start_end = []

    for i in range(count):
        temp_1, temp_2 = map(int, sys.stdin.readline().rstrip().split(" "))
        if temp_1 <= temp_2:
            start_end.append((-temp_1, temp_2))
        else:
            start_end.append((-temp_2, temp_1))
    heapq.heapify(start_end)
    distance = int(sys.stdin.readline().rstrip())
    max_result = 0
    temp = []

    while start_end:
        value = heapq.heappop(start_end)
        start = -value[0]
        end = -value[0] + distance

        if abs(value[1] + value[0]) <= distance:
            heapq.heappush(temp, -value[1])

        while temp:
            pop_value = heapq.heappop(temp)
            if -pop_value <= end:
                heapq.heappush(temp,pop_value)
                break

        if max_result <= len(temp):
            max_result = len(temp)

    print(max_result)
