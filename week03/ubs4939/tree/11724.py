import sys

sys.setrecursionlimit(10**7)

def dfs(start_node):
    if not visited_list[start_node]:
        visited_list[start_node] = True

    for next_node in node_list[start_node]:
        if not visited_list[next_node]:
            dfs(next_node)


if __name__ == '__main__':
    node_count, edge_count = map(int, sys.stdin.readline().rstrip().split(" "))
    node_list = [[] for x in range(node_count + 1)]
    visited_list = [False for x in range(node_count + 1)]
    for _ in range(edge_count):
        start, end = map(int, sys.stdin.readline().rstrip().split(" "))
        node_list[start].append(end)
        node_list[end].append(start)

    visited_list[0] = True

    group_count = 0

    while visited_list.count(True) != node_count+1:

        start_root = 0
        for index in range(1, len(visited_list)):
            if not visited_list[index]:
                start_root = index
                break

        dfs(start_root)
        group_count+=1

        if visited_list.count(True) == node_count+1:
            break

    print(group_count)
