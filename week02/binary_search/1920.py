# 재귀로 풀었더니 메모리 초과
# 재귀는 함수를 계속호출하기 때문에 while 보다 메모리를 많이 사용함.


import sys

def check_count(check_list, i, start, end):
    mid = (start + end) // 2

    if check_list[mid] == i:
        return 1
    elif start == end:
        return 0
    elif check_list[mid] < i:
        return check_count(check_list, i, mid+1, end)
     # check_list[mid] > i:
    else:
        return check_count(check_list, i, start, mid-1)


if __name__ == '__main__':
    number_count = int(sys.stdin.readline().rstrip())

    check_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    check_list.sort()

    int(sys.stdin.readline().rstrip())

    num_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    for i in num_list:
        print(check_count(check_list, i, 0, len(check_list)-1))

    # for i in num_list:
    #     start = 0
    #     end = len(check_list)-1
    #     check = 0
    #     while start <= end:
    #         mid = (start + end) // 2
    #         if check_list[mid] == i:
    #             check = 1
    #             break
    #         if check_list[mid] < i:
    #             start = mid+1
    #         elif check_list[mid] > i:
    #             end = mid -1
    #     print(check)
