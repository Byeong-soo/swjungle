import collections
import sys


def bfs(root,group):
    queue = collections.deque([root])
    visited_list[root] = True
    group_list[root] = group

    while queue:

        pop_queue = queue.popleft()

        for i in node_list[pop_queue]:
            # 방문 안했을 때
            if not visited_list[i]:
                # 큐에 넣어주고
                queue.append(i)
                # 방문 기록 남기고
                visited_list[i] = True
                # 앞에서와는 다른 그룹 지정해준다
                group_list[i] = -group_list[pop_queue]
            # 방문을 했던곳 다시 올 때
            elif visited_list[i]:
                # 연결된곳이 같은 그룹이면 바로 폴스 리턴
                if group_list[i] == group_list[pop_queue]:
                    return False

    return True




if __name__ == '__main__':
    test_count = int(sys.stdin.readline().rstrip())

    while test_count > 0:
        check = True
        node_count, edge_count = map(int, sys.stdin.readline().rstrip().split(" "))
        node_list = [[] for x in range(node_count + 1)]
        # 미방문 0, 1 or 2
        visited_list = [False for x in range(node_count + 1)]
        group_list = [0 for x in range(node_count+1)]

        for _ in range(edge_count):
            start, end = map(int, sys.stdin.readline().rstrip().split(" "))
            node_list[start].append(end)
            node_list[end].append(start)

        for i in range(1,len(visited_list)):
            if not visited_list[i]:
                check = bfs(i,1)
            if not check:
                break
        test_count -= 1

        if check:
            print("YES")
        else:
            print("NO")
