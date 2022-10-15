import sys

sys.setrecursionlimit(10 ** 7)
def dfs(start):

    visited_list[start] = True

    for computer in computer_list[start]:
        if not visited_list[computer]:
            visited_list[computer] = True
            dfs(computer)

if __name__ == '__main__':
    computer_count = int(sys.stdin.readline().rstrip())
    connect_count = int(sys.stdin.readline().rstrip())

    computer_list = [[] for x in range(computer_count + 1)]
    visited_list = [False for x in range(computer_count + 1)]
    for i in range(connect_count):
        start, end = map(int,sys.stdin.readline().rstrip().split(" "))
        computer_list[start].append(end)
        computer_list[end].append(start)

    dfs(1)
    count=0
    for visited in visited_list:
        if visited:
            count+=1

    print(count-1)