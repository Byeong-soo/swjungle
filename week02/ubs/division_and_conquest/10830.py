import sys


def mul_matrix(matrix, number):
    temp_num = number // 2
    temp_extra_num = number % 2
    result = []

    if number == 1:
        result += matrix

        for a in range(len(matrix)):
            for b in range(len(matrix)):
                matrix[a][b] = matrix[a][b] % 1000

        return result

    if temp_num > 0:
        mul_result_matrix = mul_matrix2(matrix, matrix)
        if temp_extra_num == 0:
            return mul_matrix(mul_result_matrix,temp_num)
        elif temp_extra_num > 0:
            return mul_matrix2(mul_matrix(mul_result_matrix, temp_num),matrix)


def mul_matrix2(matrix, matrix2):
    new_matrix = []
    for i in range(len(matrix)):
        temp = []
        new_matrix.append(temp)

    for large in range(len(matrix)):
        for first in range(len(matrix)):
            val = 0
            for second in range(len(matrix)):
                val += matrix[large][second] * matrix2[second][first]
            new_matrix[large].append(val % 1000)
    return new_matrix


if __name__ == '__main__':
    size, number = map(int, sys.stdin.readline().rstrip().split(" "))
    matrix = []
    for i in range(size):
        temp = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        matrix.append(temp)

    answer = mul_matrix(matrix, number)

    for num in answer:
        for j in range(len(num)):
            print(num[j],end=" ")
        print()