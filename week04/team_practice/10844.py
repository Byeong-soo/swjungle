import sys

if __name__ == '__main__':
    number = int(sys.stdin.readline().rstrip())

    stairs = [[0] * 10 for _ in range(number + 1)]

    stairs[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(2, number + 1):
        stairs[i][0] = stairs[i - 1][1]
        stairs[i][9] = stairs[i - 1][8]

        for x in range(1, 9):
            stairs[i][x] = stairs[i - 1][x - 1] + stairs[i - 1][x + 1]

    print(sum(stairs[number]) % 1000000000)
