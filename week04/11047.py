import sys

if __name__ == '__main__':
    coin_kind_count, target_price = map(int, sys.stdin.readline().rstrip().split(" "))
    coin_list = []

    for i in range(coin_kind_count):
        coin_list.append(int(sys.stdin.readline().rstrip()))
    count = 0
    while coin_list or target_price != 0:
        pop_coin = coin_list.pop()

        count += target_price // pop_coin
        target_price %= pop_coin

    print(count)
