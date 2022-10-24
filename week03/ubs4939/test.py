# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# miro_list = [list(input().strip()) for _ in range(N)]
#
# queue = deque()
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# def bfs(start):
#     queue.append(start)
#     while queue:
#         i, j, count = queue.popleft()
#         miro_list[i][j] = "0"
#         if i == N-1 and j == M-1:
#             print(count+1)
#             break
#         for k in range(4):
#             new_i = i+dx[k]
#             new_j = j+dy[k]
#             if 0 <= new_i <N and 0<= new_j <M and miro_list[new_i][new_j] == "1":
#                 queue.append([new_i, new_j, count+1])
#
# bfs([0,0,0])
#
#
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

miro_list = []

for _ in range(N):
    miro_list.append(list(map(int, input().strip())))

queue = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(start):
    queue.append(start)
    while queue:
        i, j, count = queue.popleft()
        miro_list[i][j] = 0
        if i == N - 1 and j == M - 1:
            print(count + 1)
            break
        for k in range(4):
            new_i = i + dx[k]
            new_j = j + dy[k]
            if 0 <= new_i < N and 0 <= new_j < M and miro_list[new_i][new_j] == 1:
                queue.append([new_i, new_j, count + 1])


bfs([0, 0, 0])
