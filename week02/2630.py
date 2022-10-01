def check_paper(paper_list, x, y, number):
    global white_count
    global blue_count

    color = paper_list[x][y]
    for i in range(x,x+number):
        for j in range(y,y+number):
            if color != paper_list[i][j]:
                check_paper(paper_list, x, y, number // 2)
                check_paper(paper_list, x + (number // 2), y, number // 2)
                check_paper(paper_list, x, y + (number // 2), number // 2)
                check_paper(paper_list, x + (number // 2), y + (number // 2), number // 2)
                return

    if color == 0:
        white_count += 1
    elif color == 1:
        blue_count += 1


if __name__ == '__main__':
    num = int(input())
    paper_list = [list(map(int, input().split(" "))) for x in range(num)]

    white_count = 0
    blue_count = 0

    check_paper(paper_list, 0, 0, num)

    print(white_count)
    print(blue_count)
