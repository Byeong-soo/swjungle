import sys

if __name__ == '__main__':
    matrix_count = int(sys.stdin.readline().rstrip())

    matrix_list = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for x in range(matrix_count)]
    count = [[0 for x in range(matrix_count)] for y in range(matrix_count)]

    for diagonal in range(1, matrix_count):
        for x in range(0, matrix_count - diagonal):
            y = x + diagonal

            if diagonal == 1:
                count[x][y] = matrix_list[x][0] * matrix_list[y][0] * matrix_list[y][1]
                continue

            count[x][y] = float('inf')

            for k in range(x, y):
                count[x][y] = min(count[x][y], count[x][k] + count[k + 1][y] + matrix_list[x][0] * matrix_list[k][1] *
                                  matrix_list[y][1])

    print(count[0][matrix_count-1])

    # 오 답
    # matrix_list = []
    # min_num = float('inf')
    # index = -1
    # total_sum = 0
    #
    # for x in range(matrix_count - 1):
    #     first, second = map(int, sys.stdin.readline().rstrip().split(" "))
    #     matrix_list.append(first)
    #
    # first, second = map(int, sys.stdin.readline().rstrip().split(" "))
    # matrix_list.append(first)
    # matrix_list.append(second)
    #
    #
    # for x in range(len(matrix_list)):
    #     if min_num > matrix_list[x]:
    #         min_num = matrix_list[x]
    #         index = x
    #
    # if index == 0:
    #     k = 1
    #     while index + k + 1 < len(matrix_list):
    #         total_sum += (matrix_list[index + k + 1]) * (matrix_list[index + k]) * matrix_list[index]
    #         k+=1
    #
    # elif index == len(matrix_list)-1:
    #     k = 1
    #     while index - k - 1 >= 0:
    #         total_sum += (matrix_list[index - k - 1]) * (matrix_list[index - k]) * matrix_list[index]
    #
    # else:
    #     k = 1
    #     while index - k - 1 >= 0 or index + k + 1 < len(matrix_list):
    #
    #         if index - k - 1 >= 0:
    #             total_sum += (matrix_list[index - k - 1]) * (matrix_list[index - k]) * matrix_list[index]
    #
    #         if index + k + 1 < len(matrix_list):
    #             total_sum += (matrix_list[index + k + 1]) * (matrix_list[index + k]) * matrix_list[index]
    #         k += 1
    #
    #     total_sum += matrix_list[0] * matrix_list[index] * matrix_list[len(matrix_list)-1]
    #
    # print(total_sum)
