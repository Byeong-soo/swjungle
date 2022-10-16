import sys

if __name__ == '__main__':
    minus_list = sys.stdin.readline().rstrip().split("-")
    number_list = []
    for number in minus_list:
        number_list.append(sum(list(map(int, number.split("+")))))
    total = int(number_list[0])
    for index in range(1, len(number_list)):
        total -= number_list[index]
    print(total)
