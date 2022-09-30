
if __name__ == '__main__':

    tree_count, need_meter = map(int,input().split(" "))
    tree_list = list(map(int,input().split(" ")))
    max_len = max(tree_list)

    answer = 0
    start = 0
    end = max_len

    while start <= end:
        total = 0

        center = (start+end) // 2

        for i in tree_list:
            get_tree = i - center
            if get_tree > 0:
                total += get_tree

        if need_meter > total:
            end = center -1
        else:
            start = center +1

    print(end)





