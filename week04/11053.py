import sys


def get_index(number):
    global mid
    start = 0
    end = len(answer_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if number >= answer_list[mid]:
            start = mi다d + 1
        elif number < answer_list[mid]:
            end = mid - 1
    return start


if __name__ == '__main__':
    sequence_count = int(sys.stdin.readline().rstrip())
    sequence_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    mid = 0
    answer_list = [sequence_list[0]]

    for sequence in range(1, sequence_count):
        if sequence_list[sequence] > answer_list[-1]:
            answer_list.append(sequence_list[sequence])
        else:
            index = get_index(sequence_list[sequence])
            answer_list[index] = sequence_list[sequence]
    print(len(answer_list))


    N = int(sys.stdin.readline())
    A = list(map(int, input().split()))
    dp = [1] * N

    for i in range(1, N) :
        for j in range(i) :
            if A[i] > A[j] :
                dp[i] = max(dp[i], dp[j]+1)

    print(max(dp))
    # LCS로는 안됌
    # sequence_matrix = [[0 for x in range(sequence_count + 1)] for y in range(sequence_count + 1)]
    # for y in range(1, len(sequence_list)):
    #     for x in range(1, len(sequence_list)):
    #
    #         if sequence_list[x] < sequence_list[y]:
    #             sequence_matrix[y][x] = sequence_matrix[y - 1][x - 1] + 1
    #
    #         else:
    #             sequence_matrix[y][x] = max(sequence_matrix[y - 1][x], sequence_matrix[y][x - 1])
    #
    # print(sequence_matrix[-1][-1])
