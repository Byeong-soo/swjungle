import sys

def check(list_):
    count_r = 0
    count_l = 0
    check = 0

    for i in range(len(list_)):
        check_text = list_.pop()
        if check_text == "(":
            if check == 0:
                return print("NO")
            else:
                check -= 1
                count_l +=1
        elif check_text == ")":
            check +=1
            count_r +=1

    if count_l == count_r:
        return print("YES")
    else:
        return print("NO")



if __name__ == '__main__':
    number = int(sys.stdin.readline().rstrip())

    for i in range(number):
        check(list(sys.stdin.readline().rstrip()))
