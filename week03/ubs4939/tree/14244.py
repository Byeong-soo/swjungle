import sys

if __name__ == '__main__':
    node_count, edge = map(int, sys.stdin.readline().rstrip().split(" "))
    extra = node_count - edge
    for x in range(extra):
        print(f'{x} {x+1}')
    for x in range(1,edge):
        print(f'{extra} {extra+ x}')