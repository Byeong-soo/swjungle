import sys


def check_num(matrix, x, y, number):
    result = []
    result += "("

    string = matrix[x][y]
    for i in range(x, x +number):
        for j in range(y, y + number):
            if string != matrix[i][j]:
                result += check_num(matrix, x, y, number // 2)
                result += check_num(matrix, x, y + (number // 2), number // 2)
                result += check_num(matrix, x + (number // 2), y, number // 2)
                result += check_num(matrix, x + (number // 2), y + (number // 2), number // 2)

                result+= ")"
                return result

    if string == "1":
        return "1"
    elif string == "0":
        return "0"


if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())

    matrix = []

    for i in range(count):
        matrix.append(list(sys.stdin.readline().rstrip()))

    print("".join(check_num(matrix, 0, 0, count)))
