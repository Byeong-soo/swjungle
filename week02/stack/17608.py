import sys

if __name__ == '__main__':
    number = int(sys.stdin.readline())

    bar_list = []

    for i in range(number):
        bar_list.append(int(sys.stdin.readline()))

    count = 0
    max_bar = bar_list[len(bar_list)-1]
    for i in range(len(bar_list)):
        bar = bar_list.pop()
        if bar > max_bar:
            max_bar = bar
            count+=1

    print(count+1)

