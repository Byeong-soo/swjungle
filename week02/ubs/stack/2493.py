import collections
import sys

# 시간 초과
if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())

    tower = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    index_list = [(0, tower[0])]

    result = [0]
    collections.deque(index_list)

    for i in range(1, len(tower)):
        index = len(index_list) - 1
        while len(index_list) >= 0:

            if len(index_list) == 0:
                result.append(0)
                index_list.append((i,tower[i]))
                break
            if tower[i] == index_list[index][1]:
                pop_tower = index_list.pop()
                result.append(pop_tower[0] + 1)
                index_list.append((i, tower[i]))
                break
            elif tower[i] > index_list[index][1]:
                index_list.pop()
                index -= 1
            elif tower[i] < index_list[index][1]:
                index_list.append((i,tower[i]))
                result.append(index_list[index][0] + 1)
                break

    for k in result:
        print(k, end=" ")
