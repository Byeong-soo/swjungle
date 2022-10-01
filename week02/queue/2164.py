import sys
from collections import deque
if __name__ == '__main__':
    number = int(sys.stdin.readline().rstrip())

    number_queue = deque([x for x in range(1,number+1)])
    while number > 1 :
        number_queue.popleft()
        temp = number_queue.popleft()
        number_queue.append(temp)
        number-=1

    print(number_queue[0])





