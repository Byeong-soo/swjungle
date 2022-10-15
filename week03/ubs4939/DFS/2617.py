import sys


def count_heavy(bead_number):
    global heavier_count

    for pick_bead in bead_heavy_list[bead_number]:
        if not bead_check_list[pick_bead]:
            bead_check_list[pick_bead] = True
            heavier_count += 1
            count_heavy(pick_bead)


def count_light(bead_number):
    global lighter_count

    for pick_bead in bead_light_list[bead_number]:
        if not bead_check_list[pick_bead]:
            bead_check_list[pick_bead] = True
            lighter_count += 1
            count_light(pick_bead)


if __name__ == '__main__':
    bead_count, compare_count = map(int, sys.stdin.readline().rstrip().split(" "))

    bead_heavy_list = [[] for x in range(bead_count + 1)]
    bead_light_list = [[] for x in range(bead_count + 1)]
    for _ in range(compare_count):
        heavier, lighter = map(int, sys.stdin.readline().rstrip().split(" "))
        bead_heavy_list[heavier].append(lighter)
        bead_light_list[lighter].append(heavier)

    target_num = (bead_count // 2) + 1
    result = set([])

    for bead in range(1, bead_count+1):
        heavier_count = 0
        bead_check_list = [False for x in range(bead_count + 1)]
        count_heavy(bead)
        if heavier_count >= target_num:
            result.add(bead)

    for bead in range(1, bead_count+1):
        lighter_count = 0
        bead_check_list = [False for x in range(bead_count + 1)]
        count_light(bead)
        if lighter_count >= target_num:
            result.add(bead)

    print(len(result))
