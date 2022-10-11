# 1991 트리 순회
import sys

input = sys.stdin.readline

N = int(input())

graph = {}
for _ in range(N):
    a, b, c = map(str, input().split())
    graph[a] = [b, c]

def post_search(root):
    if root != ".":
        print(root, end='')
        left, right = graph[root]
        post_search(left)
        post_search(right)


def mid_search(root):
    if root != ".":
        left, right = graph[root]
        mid_search(left)
        print(root, end='')
        mid_search(right)


def back_search(root):
    if root != ".":
        left, right = graph[root]
        back_search(left)
        back_search(right)
        print(root, end='')


post_search("A")
print()
mid_search("A")
print()
back_search("A")
