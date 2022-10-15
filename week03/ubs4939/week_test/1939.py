import sys

def dfs(start):

    end = start[0]
    weight = start[1]


    for node in node_list[end]:

        if not visited_list[node[0]]:
            visited_list[node[0]] = True





if __name__ == '__main__':
    node_count, edge_count = map(int, sys.stdin.readline().rstrip().split(" "))
    node_list = [[] for x in range(node_count + 1)]
    visited_list = [False for x in range(node_count)]

    for i in range(edge_count):
        start, end, weight = (map(int, sys.stdin.readline().rstrip().split(" ")))
        node_list[start].append((end,weight))
        node_list[end].append((start,weight))

