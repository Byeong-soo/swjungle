import sys


def dfs(y, x):
    global count
    direction_x = [1, -1, 0, 0]
    direction_y = [0, 0, 1, -1]

    if x == width - 1 and y == height - 1:
        return dp[y][x]

    for i in range(4):
        change_x = x + direction_x[i]
        change_y = y + direction_y[i]

        if 0 > change_x or 0 > change_y or change_y >= height or change_x >= width:
            continue

        if matrix[y][x] < matrix[change_y][change_x]:
            continue

        if visited[change_y][change_x]:
            # dp[y][x] += dp[change_y][change_x]
            return dp[change_y][change_x]
        visited[change_y][change_x] = True

        dp[y][x] += dfs(change_y, change_x)

    return dp[y][x]

if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().rstrip().split(" "))

    matrix = []
    for x in range(height):
        matrix.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

    dp = [[0 for x in range(width)] for y in range(height)]
    visited = [[False for x in range(width)] for y in range(height)]
    dp[height - 1][width - 1] = 1
    count = 0
    print(dfs(0, 0))
    print(matrix)
    print(dp)
