import heapq
import sys


def find(find_parent):
    if find_parent == parents_list[find_parent]:
        return find_parent
    return find(parents_list[find_parent])

def union(first,second):
    first_parent = find(first)
    second_parent = find(second)

    if first_parent != second_parent:
        if first_parent > second_parent:
            parents_list[first_parent] = second_parent
        else:
            parents_list[second_parent] = first_parent


if __name__ == '__main__':
    node_count, edge_count = map(int,sys.stdin.readline().rstrip().split(" "))
    parents_list = [x for x in range(node_count + 1)]
    visited_list = [False for x in range(node_count + 1)]

    heapq_edge = []
    for _ in range(edge_count):
        start, end, weight = map(int,sys.stdin.readline().rstrip().split(" "))
        heapq.heappush(heapq_edge,(weight,start,end))

    weight = 0

    while heapq_edge:

        heappop = heapq.heappop(heapq_edge)

        first_p = find(heappop[1])
        second_p = find(heappop[2])

        if first_p != second_p:
            union(first_p,second_p)
            weight += heappop[0]


    print(weight)
