import sys

sys.setrecursionlimit(10**7)

def bfs(start):

    for x in node_list[start]:
        if result[x] == 0:
            result[x] = start
            bfs(x)


if __name__ == '__main__':
    node_count = int(sys.stdin.readline().rstrip())

    node_list = [[] for x in range(node_count + 1)]
    result = [0 for x in range(node_count + 1)]
    for i in range(node_count-1):
        start, end = map(int,sys.stdin.readline().rstrip().split(" "))
        node_list[start].append(end)
        node_list[end].append(start)

    result[1] = 1
    bfs(1)
    print(*result[2:])