# 전위 순위는 깊이 탬색
import sys


def check_front(list_, root):
    print(root,end="")
    if list_[root][0] !=".":
        check_front(list_, list_[root][0])
    if list_[root][1] != ".":
        check_front(list_, list_[root][1])


def check_middle(list_, root):
    if list_[root][0] !=".":
        check_middle(list_, list_[root][0])
    print(root,end="")
    if list_[root][1] != ".":
        check_middle(list_, list_[root][1])


def check_end(list_, root):
    if list_[root][0] !=".":
        check_end(list_, list_[root][0])
    if list_[root][1] != ".":
        check_end(list_, list_[root][1])
    print(root,end="")
    # if num * 2 > count:
    #     return result
    # # 왼쪽 값이 존재
    # if list_[(num * 2) + 1] != ".":
    #     return result + check_front(list_,num*2+1,count)
    # # 왼쪽 값이 없음
    # # elif list_[num * 2] == ".":
    # # 오른쪽 값이 존재
    # if list_[(num * 2) + 2] != ".":
    #     return result + check_front(list_,num*2+2,count)
    # # 오른쪽 값이 없음
    # # elif list_[(num * 2) + 1] == ".":


if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())

    number_list = {}

    for _ in range(count):
        root, left, right = sys.stdin.readline().rstrip().split(" ")
        number_list[root] = left, right

    first_root = next(iter(number_list))

    check_front(number_list, first_root)
    print()
    check_middle(number_list, first_root)
    print()
    check_end(number_list,first_root)
