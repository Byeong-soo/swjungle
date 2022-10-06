import copy
import sys
import heapq

if __name__ == '__main__':
    number_count = int(sys.stdin.readline().rstrip())
    number_list_max = []
    number_list_min = []
    global result

    for i in range(0, number_count):
        num = int(sys.stdin.readline().rstrip())

        if len(number_list_max) == len(number_list_min):
            heapq.heappush(number_list_min,(-num,num))
        else:
            heapq.heappush(number_list_max, (num,num))

        if number_list_max and number_list_min and number_list_min[0][1] > number_list_max[0][1]:
            lower_num = heapq.heappop(number_list_max)[1]
            bigger_num = heapq.heappop(number_list_min)[1]

            heapq.heappush(number_list_max,(bigger_num,bigger_num))
            heapq.heappush(number_list_min,(-lower_num,lower_num))

        print(number_list_min[0][1])