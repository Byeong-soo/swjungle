import itertools
import math
import sys


def fibonacci_numbers(num):
    first = 0
    second = 1
    tmep = 0

    while num - 1 != 0:
        temp = first
        first = second
        second = (temp + second)% 15746

        num -= 1
    return second


if __name__ == '__main__':
    number = int(sys.stdin.readline().rstrip())

    print(fibonacci_numbers(number + 1))

    # dp =[0] * 1000001
    # dp[1] =1
    # dp[2] = 2
    # for i in range(3, number+1):
    #     dp[i] = (dp[i-2]+dp[i-1]) % 15746
    # print(dp[number])

    # 규칙성 찾아서 콤비네이션 , 시간초과
    # k = 0
    # total_sum = 0
    # while number - (2 * k) >= 0:
    #     calculate = math.comb(number - k, k)
    #     total_sum += calculate
    #     k += 1

