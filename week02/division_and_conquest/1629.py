import sys


#
# def get_extra(num, num2, num3):
#     temp_num = num // num3
#     result = 1
#
#     if num2 < 2:
#         return result
#
#     if temp_num < 1:
#         log = math.ceil(math.log(num3, num))
#         temp2 = num2 // log
#         temp3 = num2 % log
#         temp4 = (num ** temp2) % num3
#
#         return result * (num ** temp3) * get_extra(temp4, temp2, num3)
#
#     else:
#         num = num % num3
#         return get_extra(num, num2, num3)
#

def check_extra2(num, num2, num3):
    temp1 = num2 // 2
    temp2 = num2 - temp1
    result = 1

    if temp1 == 0:
        result *= (num % num3)
        return result

    if num2 % 2 == 0:
        return (result * (check_extra2(num, temp1, num3) ** 2)) % num3
    else:
        return (result * check_extra2(num, temp1, num3) * check_extra2(num, temp2, num3)) % num3


if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))

    print(check_extra2(a, b, c))