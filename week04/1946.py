import heapq
import sys

if __name__ == '__main__':
    test_case_count = int(sys.stdin.readline().rstrip())

    for _ in range(test_case_count):
        people_number = int(sys.stdin.readline().rstrip())
        grade_list = []
        for _ in range(people_number):
            first, second = (map(int, sys.stdin.readline().rstrip().split(" ")))
            grade_list.append((first, second))

        grade_list.sort(key=lambda x: x[0])

        standard = grade_list[0][0] + grade_list[0][1]
        num = 0
        for x in range(1, people_number):
            if grade_list[x][0] + grade_list[x][1] < standard:
                standard = grade_list[x][0] + grade_list[x][1]
                continue
            elif grade_list[x][0] + grade_list[x][1] > standard:
                num += 1
            standard+=1

        print(people_number - num)
