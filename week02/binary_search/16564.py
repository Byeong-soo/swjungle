if __name__ == '__main__':

    character_count, total_count = map(int, input().split(" "))
    character_list = [int(input()) for x in range(character_count)]
    start = min(character_list)
    end = max(character_list) + total_count
    result = start
    while start <= end:
        mid = (start + end) // 2
        l = 0
        for i in character_list:
            gap = mid - i
            if gap > 0:
                l += gap
        if l <= total_count:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    print(result)
