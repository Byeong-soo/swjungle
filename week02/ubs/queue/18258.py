from collections import deque
import sys

if __name__ == '__main__':
    number = int(sys.stdin.readline())

    queue_ = deque()
    rear = -1
    for i in range(number):
        order = (sys.stdin.readline().rstrip())
        if "push" in order:
            queue_.append(order.split(" ")[1])
            rear +=1
        elif order == "pop":
            if queue_:
                print(queue_.popleft())
                rear -=1
            else:
                print(-1)
        elif order == "size":
            print(len(queue_))
        elif order == "front":
            print(queue_[0]) if queue_ else print(-1)
        elif order == "back":
            print(queue_[rear]) if queue_ else print(-1)
        elif order == "empty":
            print(0) if queue_ else print(1)
