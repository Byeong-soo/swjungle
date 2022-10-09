import collections
import sys

sys.setrecursionlimit(10**9)

def search_path(start_node):
    global count
    count = 0

    visited_list[start_node] = True
    for next_node in node_list[start_node]:
        next_attr = node_attr_list[next_node]
        if next_attr == 1:
            count += 1
        else:
            if not visited_list[next_node]:
                count += search_path(next_node)
    return count


if __name__ == '__main__':
    node_count = int(sys.stdin.readline().rstrip())
    node_attr_list = list(map(int, [2] + list(sys.stdin.readline().rstrip())))
    node_list = [[] for x in range(node_count + 1)]
    edge_count = node_count - 1
    visited_list = [False for x in range(node_count + 1)]
    count = 0
    total_sum = 0
    inner_sum = 0

    for _ in range(node_count - 1):
        start, end = map(int, sys.stdin.readline().rstrip().split(" "))
        node_list[start].append(end)
        node_list[end].append(start)


    for start in range(1, node_count + 1):
        if node_attr_list[start] == 1:
            for x in node_list[start]:
                if node_attr_list[x] == 1:
                    inner_sum += 1
        else:
            if visited_list[start]:
                continue
            count = search_path(start)
            total_sum += count * (count-1)

    print(total_sum + inner_sum)
