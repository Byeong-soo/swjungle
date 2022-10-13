import sys

sys.setrecursionlimit(10 ** 7)

def dfs(start, group):
    global check
    if check:
        return

    for x in node_list[start]:

        if not visited_list[x]:
            group_list[x] = -group
            visited_list[x] = True
            dfs(x, -group)
        elif visited_list[x]:
            if group_list[start] == group_list[x]:
                check = True
                return



if __name__ == '__main__':
    testcase_count = int(sys.stdin.readline().rstrip())

    for i in range(testcase_count):
        node_count, edge_count = map(int, sys.stdin.readline().rstrip().split(" "))

        check = False
        visited_list = [False for x in range(node_count + 1)]
        group_list = [0 for z in range(node_count + 1)]
        node_list = [[] for y in range(node_count + 1)]
        for x in range(edge_count):
            start, end = map(int, sys.stdin.readline().rstrip().split(" "))
            node_list[start].append(end)
            node_list[end].append(start)

        group = 1
        group_list[1] = 1

        for node in range(1,node_count+1):
            if not visited_list[node]:
                dfs(node,group)

        if not check:
            print("YES")
        else:
            print("NO")
