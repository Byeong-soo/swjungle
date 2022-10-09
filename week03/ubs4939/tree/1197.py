import heapq
import sys


def find_parent(parent_list, find_node):
    if parent_list[find_node] == find_node:
        return find_node
    return find_parent(parent_list, parent_list[find_node])


def union(parent_list, first_node, second_node):
    p_first_node = find_parent(parent_list, first_node)
    p_second_node = find_parent(parent_list, second_node)

    if p_first_node == p_second_node:
        return

    if p_first_node > p_second_node:
        parent_list[p_first_node] = p_second_node
    else:
        parent_list[p_second_node] = p_first_node


if __name__ == '__main__':
    node_count, edge_count = map(int, sys.stdin.readline().rstrip().split(" "))

    edge_list = []
    parent_list = [x for x in range(node_count + 1)]

    for x in range(edge_count):
        start, end, weight = map(int, sys.stdin.readline().rstrip().split(" "))
        heapq.heappush(edge_list, [weight, start, end])

    total_sum = 0

    while edge_list:

        min_pop = heapq.heappop(edge_list)

        node_weight = min_pop[0]
        node_start = min_pop[1]
        node_end = min_pop[2]

        parent1 = find_parent(parent_list, node_start)
        parent2 = find_parent(parent_list, node_end)

        if parent1 != parent2:
            total_sum += node_weight
            union(parent_list, node_start, node_end)

    print(total_sum)
