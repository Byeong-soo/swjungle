import sys

# 시간 복잡도
# while 하나, O(n)

# 공간 복잡도
# O(4)

def fibonacci_numbers(num):
    first = 0
    second = 1
    tmep = 0

    while num - 1 != 0:
        temp = first
        first = second
        second = temp + second

        num -= 1
    return second


if __name__ == '__main__':
    number = int(sys.stdin.readline().rstrip())

    print(fibonacci_numbers(number))
