import sys


def preorder(root):
    print(root, end="")
    if number_dic[root][0] != ".":
        preorder(number_dic[root][0])
    if number_dic[root][1] != ".":
        preorder(number_dic[root][1])


def inorder(root):
    if number_dic[root][0] != ".":
        inorder(number_dic[root][0])
    print(root, end="")
    if number_dic[root][1] != ".":
        inorder(number_dic[root][1])


def postorder(root):
    if number_dic[root][0] != ".":
        postorder(number_dic[root][0])
    if number_dic[root][1] != ".":
        postorder(number_dic[root][1])
    print(root, end="")


if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())

    number_dic = {}
    key_list = []

    for _ in range(count):
        root, left, right = sys.stdin.readline().rstrip().split(" ")
        number_dic[root] = [left, right]
        key_list.append(root)

    keys = number_dic.keys()
    preorder(key_list[0])
    print("")
    inorder(key_list[0])
    print("")
    postorder(key_list[0])
