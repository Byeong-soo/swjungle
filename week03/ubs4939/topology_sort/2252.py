import collections
import sys


def line_up():
    global result
    deque_student = collections.deque([])

    for x in range(1,student_count + 1):
        if indegree_count[x] == 0:
            deque_student.append(x)

    while deque_student:

        pop_student = deque_student.popleft()
        result.append(pop_student)

        for student in student_list[pop_student]:
            indegree_count[student] -= 1
            if indegree_count[student] == 0:
                deque_student.append(student)


if __name__ == '__main__':
    student_count, compare_count = map(int, sys.stdin.readline().rstrip().split(" "))

    student_list = [[] for x in range(student_count + 1)]
    indegree_count = [0 for x in range(student_count + 1)]
    result = []

    for x in range(compare_count):
        first, second = map(int, sys.stdin.readline().rstrip().split(" "))
        student_list[first].append(second)
        indegree_count[second] += 1

    line_up()
    print(*result)
