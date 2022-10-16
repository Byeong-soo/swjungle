import sys

if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())

    value_list = [(1,0) for x in range(46)]

    for x in range(1,count+1):
        value_list[x] = (value_list[x-1][1], value_list[x-1][0] + value_list[x-1][1])

    print(*value_list[count])


