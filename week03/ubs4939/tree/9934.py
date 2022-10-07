import sys


def inorder(root,depth):

    left = (2*root) +1
    right = (2*root) +2

    if left >= (2**depth) -1 and building_list[root] is None:
        building_list[root] = inorder_list[0]
        del inorder_list[0]
        return

    inorder(left,depth)

    building_list[root] = inorder_list[0]
    del inorder_list[0]

    if right >= (2**depth) -1 and building_list[root] is None:
        building_list[root] = inorder_list[0]
        del inorder_list[0]
        return

    inorder(right,depth)



if __name__ == '__main__':
    depth = int(sys.stdin.readline().rstrip())
    inorder_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    building_list = [None] * ((2 ** depth) - 1)
    inorder(0,depth)

    for x in range(1,depth+1):
        for y in range(2**(x-1)):
            print(building_list[2**(x-1)-1+y],end=" ")
        print()

