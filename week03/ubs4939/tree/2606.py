import sys


def dfs(root_node):
    if not visited_list[root_node]:
        visited_list[root_node] = True

    for next_num in computer_linked_list[root_node]:
        if not visited_list[next_num]:
            dfs(next_num)


if __name__ == '__main__':
    computer_count = int(sys.stdin.readline().rstrip())
    edge_count = int(sys.stdin.readline().rstrip())

    computer_linked_list = [[] for x in range(computer_count + 1)]
    visited_list = [False for x in range(computer_count + 1)]

    for _ in range(edge_count):
        start, end = map(int, sys.stdin.readline().rstrip().split(" "))
        computer_linked_list[start].append(end)
        computer_linked_list[end].append(start)

    count = 0
    dfs(1)
    for visited in visited_list:
        if visited:
            count += 1

    print(count - 1)
