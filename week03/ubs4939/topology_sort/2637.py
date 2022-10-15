import collections
import sys

if __name__ == '__main__':
    target_number = int(sys.stdin.readline().rstrip())
    ex_count = int(sys.stdin.readline().rstrip())

    tree = [[0 for y in range(target_number + 1)] for x in range(target_number + 1)]
    connection = [[] for _ in range(target_number + 1)]
    count_list = [0 for x in range(target_number + 1)]
    indegree_count = [0 for x in range(target_number + 1)]

    for _ in range(ex_count):
        middle, basic, count = (map(int, sys.stdin.readline().rstrip().split(" ")))
        connection[basic].append((middle,count))
        indegree_count[middle] += 1

    deque_target = collections.deque([])

    for x in range(1, target_number + 1):
        if indegree_count[x] == 0:
            deque_target.append(x)

    while deque_target:
        pop_toy = deque_target.popleft()

        for toy,need_count in connection[pop_toy]:
            if tree[pop_toy].count(0) == target_number + 1:
                tree[toy][pop_toy] += need_count
            else:
                for i in range(1, target_number+1):
                    tree[toy][i] += tree[pop_toy][i] * need_count
            indegree_count[toy] -=1
            if indegree_count[toy] == 0:
                deque_target.append(toy)

    for toy,need  in enumerate(tree[target_number]):
        if need >0:
            print(f'{toy} {need}')

