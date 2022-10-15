import sys

if __name__ == '__main__':
    test_count = int(sys.stdin.readline().rstrip())

    for _ in range(test_count):

        coin_count = int(sys.stdin.readline().rstrip())
        coin_list = list(map(int,sys.stdin.readline().rstrip().split(" ")))
        target_price = int(sys.stdin.readline().rstrip())
        make_coin = [0 for z in range(target_price+1)]
        make_coin[0] = 1

        for coin in coin_list:
            for x in range(target_price + 1):
                if x - coin >= 0:
                    make_coin[x] += make_coin[x-coin]

        print(make_coin[target_price])


