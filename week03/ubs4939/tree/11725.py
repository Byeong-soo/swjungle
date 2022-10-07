import sys

sys.setrecursionlimit(10 ** 6)


def dfs(start, number_list, parents):

    for i in number_list[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, number_list, parents)


if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())
    number_list = [[] for x in range(count+1)]
    parent = [0 for x in range(count+1)]

    for _ in range(count - 1):
        f_num, s_num = map(int, sys.stdin.readline().rstrip().split(" "))
        number_list[f_num].append(s_num)
        number_list[s_num].append(f_num)

    dfs(1,number_list,parent)

    for x in range(2,len(parent)):
        print(parent[x])
