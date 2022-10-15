import sys

if __name__ == '__main__':
    first_list =['-']+list(sys.stdin.readline().rstrip())
    second_list =['-']+list(sys.stdin.readline().rstrip())

    match_list = [[0 for x in range(len(second_list))] for y in range(len(first_list))]

    for first in range(1,len(first_list)):
        for second in range(1,len(second_list)):

            if first_list[first] == second_list[second]:
                match_list[first][second] = match_list[first-1][second-1] + 1
            elif first_list[first] != second_list[second]:
                match_list[first][second] = max(match_list[first -1][second],match_list[first][second-1])

    print(match_list[len(first_list)-1][len(second_list)-1])