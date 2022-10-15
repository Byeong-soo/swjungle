import sys

sys.setrecursionlimit(10 ** 9)


def find_inner_near_out(start):
    global inner
    visited_list[start] = True
    for node in edge_list[start]:
        if attr_list[node] == 1:
            inner += 1
        else:
            if not visited_list[node]:
                visited_list[node] = True
                find_inner_near_out(node)


if __name__ == '__main__':
    node_count = int(sys.stdin.readline().rstrip())
    attr_list = [9] + list(map(int, list(sys.stdin.readline().rstrip())))

    visited_list = [False for x in range(node_count + 1)]

    edge_list = [[] for x in range(node_count + 1)]

    inner_to_inner_sum = 0
    total_sum = 0

    for x in range(node_count - 1):
        start, end = map(int, sys.stdin.readline().rstrip().split(" "))
        edge_list[start].append(end)
        edge_list[end].append(start)

    for x in range(1, node_count + 1):
        if attr_list[x] == 1:
            for y in edge_list[x]:
                if attr_list[y] == attr_list[x]:
                    inner_to_inner_sum += 1
        elif attr_list[x] == 0:
            if not visited_list[x]:
                inner = 0
                find_inner_near_out(x)
                total_sum += inner * (inner - 1)

    print(total_sum + inner_to_inner_sum)
