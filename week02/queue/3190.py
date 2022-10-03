import collections
import sys


def change_direction(state, direction):
    if state == "D":
        if direction == "D":
            return "W"
        elif direction == "L":
            return "U"

    if state == "L":
        if direction == "D":
            return "U"
        elif direction == "L":
            return "W"

    if state == "W":
        if direction == "D":
            return "L"
        if direction == "L":
            return "D"

    if state == "U":
        if direction == "D":
            return "D"
        if direction == "L":
            return "L"


def move(state, position):
    if state == "D":
        position[1] += 1
    elif state == "L":
        position[1] -= 1
    elif state == "U":
        position[0] -= 1
    elif state == "W":
        position[0] += 1
    return position


if __name__ == '__main__':
    board_size = int(sys.stdin.readline().rstrip())
    apple_count = int(sys.stdin.readline().rstrip())
    apple_position = []

    for i in range(apple_count):
        apple_position.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

    move_direction_count = int(sys.stdin.readline().rstrip())
    move_direction_list = []

    for i in range(move_direction_count):
        move_direction_list.append(list(sys.stdin.readline().rstrip().split()))
        move_direction_list[i][0] = int(move_direction_list[i][0])

    move_direction_list = collections.deque(move_direction_list)
    board = [[0 for x in range(board_size)] for y in range(board_size)]

    for i in range(apple_count):
        x = apple_position[i][0]
        y = apple_position[i][1]

        board[x - 1][y - 1] = 2

    direction = "D"
    time = 0

    position = collections.deque([[0, 0]])

    po = [0, 0]

    last_time = int(move_direction_list[len(move_direction_list) - 1][0])
    command = move_direction_list[0]
    move_direction_list.popleft()

    while 0 <= po[0] < board_size and 0 <= po[1] < board_size:

        time += 1

        po = move(direction, po)

        if po[0] < 0 or po[0] >= board_size or po[1] < 0 or po[1] >= board_size:
            break

        if po in position:
            break

        if board[po[0]][po[1]] == 2:
            position.append([po[0], po[1]])
            board[po[0]][po[1]] = 0
        else:
            position.append([po[0], po[1]])
            position.popleft()

        if command[0] == time:
            direction = change_direction(direction, command[1])
            if len(move_direction_list) > 0:
                command = move_direction_list[0]
                move_direction_list.popleft()

    print(time)
