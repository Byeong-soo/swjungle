import sys


def solution(i, route):
    # 0 이 아니다. 이미 방문한 적이 있는 이다. (갈수 있는 곳이다)
    if dp[i][route] != 0:
        return dp[i][route]

    # 첫번쨰를 재외하고 마지막 방문지이다.
    if route == (1 << (n - 1)) - 1:
        if graph[i][0]:
            return graph[i][0]
        else:
            return 1e9

    bound = 1e9

    for j in range(1, n):
        # 그래프가 0 이면 컴티뉴( 못가는 곳이니까)
        if not graph[i][j]:
            continue
        # route 가 1 << j -1 에 포함되어있다.
        # 이미 다녀온 곳임
        if route & (1 << j - 1):
            continue
        # i 출발 목적지 j,
        # i 가 0일떄 j가 1 이면 [0][1] 처음에서 두번쨰 도시하는거. 플러스
        # 첫번째 도시에서(0|1<<0) 이므로 루트는 1이 된다 (도시하나만 방문)
        dist = graph[i][j] + solution(j, route | (1 << (j - 1)))
        if bound > dist:
            bound = dist
    dp[i][route] = bound

    return bound


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dp = [[0] * (1 << n - 1) for _ in range(n)]

    print(solution(0, 0))
    print(dp)
