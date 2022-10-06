import itertools
import math

if __name__ == '__main__':
    home_count, wifi_count = map(int, input().split(" "))
    home_index = [int(input()) for x in range(home_count)]
    home_index.sort()
    result = 0
    start, end = 1, home_index[home_count - 1]

    if wifi_count == 2:
        print(home_index[home_count - 1] - home_index[0])
    else:
        while start < end:
            mid = (start + end) // 2
            last_position = home_index[0]
            count = 1

            for i in home_index:
                if i - last_position >= mid:
                    last_position = i
                    count += 1
            if count >= wifi_count:
                result = mid
                start = mid + 1
            elif count < wifi_count:
                end = mid
        print(result)

    #
    #
    #     while not check:
    #         while wifi_count > 0:
    #
    #             if n + i > home_count - 1:
    #                 average -= 1
    #                 break
    #
    #             if home_index[n + i] - home_index[n] >= average:
    #                 n = n + i
    #                 wifi_count -= 1
    #                 i = 1
    #
    #                 if wifi_count == 0:
    #                     check = True
    #                     break
    #             else:
    #                 i += 1
    # print(average)

    # start = 0
    # end = (home_count-1)
    # wifi_count -=2
    # depth = 1
    # min_len = home_index[end] - home_index[start]
    #
    # while start <= end:
    #     mid = round((start + end) // 2)
    #     if home_index[mid] - home_index[start] < home_index[end] - home_index[mid]:
    #         min_len = home_index[mid] - home_index[start]
    #         start = mid
    #     else:
    #         min_len = home_index[end] - home_index[mid]
    #         end = mid
    #     wifi_count -= depth * 2**(depth-1)
    #
    #     if wifi_count <= 0:
    #         break
    #
    #     depth+=1
    #
    # print(min_len)
