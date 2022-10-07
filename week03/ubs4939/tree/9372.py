import sys


def check_airplane(start, country_list, visited_county):
    visited_county[start] = True
    count = 0
    for x in country_list[start]:
        if not visited_county[x]:
            count += 1
            count += check_airplane(x, country_list, visited_county)

    return count


if __name__ == '__main__':
    testcase_count = int(sys.stdin.readline().rstrip())

    for i in range(testcase_count):
        country_count, airplane_count = map(int, sys.stdin.readline().rstrip().split(" "))
        country_list = [[] for x in range(country_count + 1)]
        visited_country = [False for x in range(country_count + 1)]

        for j in range(airplane_count):
            start, end = map(int, sys.stdin.readline().rstrip().split(" "))
            country_list[start].append(end)
            country_list[end].append(start)

        print(check_airplane(1,country_list,visited_country))