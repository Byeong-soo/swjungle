import sys
from collections import defaultdict
from heapq import heappop, heappush

n = int(sys.stdin.readline().rstrip())
graph = defaultdict(list)
out_degree = [0] * (n+1)

for i in range(1, n+1):
    tmp = sys.stdin.readline().rstrip()
    for j in range(n):
        if tmp[j] == '1':
            graph[j+1].append(i)
            out_degree[i] += 1


rank = [0] * (n+1)
def bfs(n):
    q = []
    for i in range(1, n+1):
        if out_degree[i] == 0:
            heappush(q, -i)
    if q == []:
        return False

    count = n
    while q:
        cur = -heappop(q)
        rank[cur] = count
        count -= 1
        for next in graph[cur]:
            out_degree[next] -= 1
            if out_degree[next] == 0:
                if rank[next] != 0:
                    return False
                heappush(q, -next)
    return True


if bfs(n):
    for r in rank[1:]:
        sys.stdout.write(f'{r} ')
else:
    sys.stdout.write('-1')