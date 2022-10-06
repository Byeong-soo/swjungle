import sys

if __name__ == '__main__':
    number_count = int(sys.stdin.readline().rstrip())

    number_stack = []

    for i in range(number_count):
        num = int(sys.stdin.readline().rstrip())

        if num == 0:
            number_stack.pop()
        else:
            number_stack.append(num)

    print(sum(number_stack))
