import sys

sys.setrecursionlimit(10**6)

def dfs(root):
    visited_list[root] = True
    for i in node_list[root]:
        if not visited_list[i]:
            visited_list[i] = True
            dfs(i)


if __name__ == '__main__':
    node_count, edge_count = map(int, sys.stdin.readline().rstrip().split(" "))

    node_list = [[] for x in range(node_count + 1)]
    visited_list = [False for x in range(node_count + 1)]
    for _ in range(edge_count):
        start, end = map(int, sys.stdin.readline().rstrip().split(" "))
        node_list[start].append(end)
        node_list[end].append(start)

    count = 0
    for i in range(1,node_count + 1):
        if not visited_list[i]:
            dfs(i)
            count += 1

    print(count)
