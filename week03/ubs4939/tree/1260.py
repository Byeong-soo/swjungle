import collections
import sys


def dfs(start):
    if not visited_list[start]:
        visited_list[start] = True
        result.append(start)

    for i in board_list[start]:
        if not visited_list[i]:
            dfs(i)
        elif visited_list[i]:
            continue


def bfs(start):
    custom_que = collections.deque([start])
    visited_list2[start] = True

    while custom_que:
        pop = custom_que.popleft()
        result2.append(pop)

        for i in board_list[pop]:
            if not visited_list2[i]:
                custom_que.append(i)
                visited_list2[i] = True


if __name__ == '__main__':
    node, line, start_node = map(int, sys.stdin.readline().rstrip().split(" "))

    board_list = [[] for x in range(node + 1)]
    visited_list = [False for x in range(node + 1)]
    visited_list2 = [False for x in range(node + 1)]
    result = []
    result2 = []

    for _ in range(line):
        start, end = map(int, sys.stdin.readline().rstrip().split(" "))
        board_list[start].append(end)
        board_list[end].append(start)

        board_list[start].sort()
        board_list[end].sort()

    dfs(start_node)
    bfs(start_node)

    print(*result)
    print(*result2)
