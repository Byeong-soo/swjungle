import sys


def is_empty(stack_):
    if len(stack_) == 0:
        return True
    elif len(stack_) >0:
        return False

def order(stack_,order_):
    if len(order_) ==2:
        stack_.append(order_[1])
    else:
        # pop
        if order_[0] == "pop":
            if is_empty(stack_):
                print(-1)
            else:
                print(stack_.pop())

        elif order_[0] == "size":
            print(len(stack_))

        elif order_[0] == "empty":
            if is_empty(stack_):
                print(1)
            else:
                print(0)

        elif order_[0] == "top":
            if is_empty(stack_):
                print(-1)
            else:
                print(stack_[len(stack_)-1])


if __name__ == '__main__':
    number = int(sys.stdin.readline().rstrip())

    stack_list = []

    for num in range(number):
        order(stack_list,list(sys.stdin.readline().rstrip().split(" ")))

