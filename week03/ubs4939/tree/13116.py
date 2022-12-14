import sys


def check_root(number):
    result = []

    if number <= 0:
        return result
    result.append(number)
    number //= 2

    return result + check_root(number)


def check_root2(number):
    if number <= 0:
        return

    if not tree[number]:
        tree[number] = True
        check_root2(number // 2)


def check_root3(number):
    if number <= 0:
        return
    if tree[number]:
        print(number * 10)
        return
    else:
        check_root3(number // 2)


if __name__ == '__main__':
    test_count = int(sys.stdin.readline().rstrip())

    for _ in range(test_count):
        tree = [False for x in range(0, 1024)]
        f_num, s_num = map(int, sys.stdin.readline().rstrip().split(" "))
        #
        # while True:
        #     if f_num == s_num:
        #         print(f_num * 10)
        #         break
        #
        #     if f_num > s_num:
        #         f_num //= 2
        #     else:
        #         s_num //= 2

        if f_num < s_num:
            temp = f_num
            f_num = s_num
            s_num =temp

        check_root2(f_num)
        check_root3(s_num)

        # result1 = check_root(f_num)
        # result2 = check_root(s_num)

        # print(result1)
        # print(result2)

        # check = False
        #
        # for num2 in result2:
        #     for num1 in result1:
        #         if num1 == num2:
        #             print(num1 * 10)
        #             check = True
        #             break
        #         elif num1 < num2:
        #             break
        #     if check:
        #         break
