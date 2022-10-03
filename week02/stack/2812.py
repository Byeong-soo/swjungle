import sys
from collections import deque

if __name__ == '__main__':
    num_size, delete_count = map(int, sys.stdin.readline().rstrip().split(" "))
    num_list = list(map(int, sys.stdin.readline().rstrip()))
    result = []

    for i in range(len(num_list)):
        while result and result[-1] < num_list[i] and delete_count > 0:
            result.pop()
            delete_count -=1
        result.append(num_list[i])
    result = list(map(str,result))
    if delete_count > 0 :
        print("".join(result[:-delete_count]))
    elif delete_count == 0:
        print("".join(result))