import sys


def find(list_, root):
    index = 0

    if root >= len(list_):
        return

    for x in range(len(list_)):
        if list_[x] > list_[root]:
            index = x
            break

    find(list_[root + 1:index], root)
    find(list_[index:len(list_)], index)
    print(list_[root])


if __name__ == '__main__':
    number_list = []

    try:
        while True:
            number_list.append(int(sys.stdin.readline().rstrip()))
    except:
        pass

    find(number_list, 0)
