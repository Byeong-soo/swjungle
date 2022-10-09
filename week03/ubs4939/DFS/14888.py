import sys


def plus_(root, value):
    return root + value


def minus_(root, value):
    return root - value


def divide_(root, value):
    if root < 0:
        result = -root // value
        return -result
    return root // value


def multiply_(root, value):
    return root * value


def dfs(depth, total, plus, minus, divide, multiply):
    global max_num
    global min_num

    if depth == number_count:
        max_num = max(total, max_num)
        min_num = min(total, min_num)

    if plus:
        dfs(depth + 1, plus_(total,number_list[depth]), plus - 1, minus, divide, multiply)
    if minus:
        dfs(depth + 1, minus_(total,number_list[depth]), plus, minus - 1, divide, multiply)
    if divide:
        dfs(depth + 1, divide_(total,number_list[depth]), plus, minus, divide - 1, multiply)
    if multiply:
        dfs(depth + 1, multiply_(total,number_list[depth]), plus, minus, divide, multiply - 1)


if __name__ == '__main__':
    number_count = int(sys.stdin.readline().rstrip())
    number_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    sign_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    max_num = -1000000000
    min_num = 1000000000

    dfs(1, number_list[0], sign_list[0], sign_list[1], sign_list[3], sign_list[2])

    print(max_num)
    print(min_num)
