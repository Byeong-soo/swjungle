import collections
import sys


def dfs(root):
    dfs_result.append(root)
    visited_list[root] = True

    for i in node_list[root]:
        if not visited_list[i]:
            visited_list[i] = True
            dfs(i)




def bfs(root):

    que_list = collections.deque([root])
    visited_list[root] = True

    while que_list:
        pop = que_list.popleft()
        bfs_result.append(pop)

        for i in node_list[pop]:
            if not visited_list[i]:
                visited_list[i] = True
                que_list.append(i)



if __name__ == '__main__':
    node_count, edge_count, root = map(int,sys.stdin.readline().rstrip().split(" "))

    bfs_result = []
    dfs_result = []
    node_list = [[] for x in range(node_count+1)]

    for _ in range(edge_count):
        start, end = map(int,sys.stdin.readline().rstrip().split(" "))
        node_list[start].append(end)
        node_list[end].append(start)
        node_list[start].sort()
        node_list[end].sort()

    visited_list = [False for x in range(node_count + 1)]
    bfs(root)
    visited_list = [False for x in range(node_count + 1)]
    dfs(root)
    print(* dfs_result)
    print(* bfs_result)