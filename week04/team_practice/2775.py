import sys

if __name__ == '__main__':
    test_count = int(sys.stdin.readline().rstrip())

    for i in range(test_count):
        people = [[0 for x in range(0, 15)] for y in range(15)]

        for x in range(15):
            people[0][x] = x
        floor = int(sys.stdin.readline().rstrip())
        room_number = int(sys.stdin.readline().rstrip())

        for y in range(1, floor + 1):
            for x in range(room_number+1):
                people[y][x] = people[y][x - 1] + people[y - 1][x]

        print(people[floor][room_number])
