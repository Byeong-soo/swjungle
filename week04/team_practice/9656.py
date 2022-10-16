import sys

if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())

    if count % 2 == 0:
        print("CY")
    else:
        print("SK")
