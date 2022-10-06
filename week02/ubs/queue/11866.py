import collections
import sys

if __name__ == '__main__':
    member, target = map(int, sys.stdin.readline().rstrip().split(" "))

    member_queue = collections.deque([str(x) for x in range(1, member + 1)])
    answer = []

    a = 0
    repeat = 0
    start_index = 0
    while member > 0:
        a = (start_index + target - 1) % member
        answer.append(member_queue[a])
        del member_queue[a]
        member -= 1
        start_index = a
    print("<", end="")
    print(", ".join(list(answer)),end="")
    print(">", end="")
