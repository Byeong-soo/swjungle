import collections
import heapq
import sys

def find_index(value,index):
    try:
        return use_list[index+1:].index(value)
    except ValueError:
        return 99999999999


if __name__ == '__main__':
    hole_number, use_number = map(int, sys.stdin.readline().rstrip().split(" "))
    use_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    socket_list = []
    num = 0

    for x in range(use_number):
        check = False
        for y in range(len(socket_list)):
            # 콘센트 안에 있을때
            if socket_list[y][1] == use_list[x]:
                socket_list[y] = (-find_index(use_list[x],x),use_list[x])
                check = True
            # 콘센트 안에 없을때
        if not check:
            # 콘센트 빈자리 있을때
            if len(socket_list) < hole_number:
                socket_list.append((-find_index(use_list[x],x),use_list[x]))
            # 콘센트 빈자리없을 때
            else:
                heapq.heapify(socket_list)
                heapq.heappop(socket_list)
                socket_list.append((-find_index(use_list[x],x),use_list[x]))
                num +=1
        for z in range(len(socket_list)):
            socket_list[z] = (-find_index(socket_list[z][1],x),socket_list[z][1])

    print(num)
    # 아쉬운 답
    # power_socket_distance = [999999 for x in range(use_number)]
    # index_list = [x for x in range(use_number)]
    # for standard in range(use_number):
    #     for compare in range(standard + 1, use_number):
    #         if use_list[standard] == use_list[compare]:
    #             power_socket_distance[standard] = compare
    #             break
    #
    # socket_list = []
    #
    # deque_index = collections.deque(index_list)
    # num = 0
    # pop_index = deque_index.popleft()
    # heapq.heappush(socket_list, (-power_socket_distance[pop_index], use_list[pop_index]))
    #
    # while deque_index:
    #     pop_index = deque_index.popleft()
    #     check = False
    #
    #     for x in range(len(socket_list)):
    #         # 같은거 찾은 (소켓에 꼽혀있음)
    #         if socket_list[x][1] == use_list[pop_index]:
    #             for socket in range(len(socket_list)):
    #                 if socket_list[socket][0] + 1 > 0:
    #                     socket_list[socket] = (-999999, socket_list[socket][1])
    #                 else:
    #                     socket_list[socket] = (socket_list[socket][0] + 1, socket_list[socket][1])
    #             socket_list[x] = (-power_socket_distance[pop_index], use_list[pop_index])
    #             check = True
    #             break
    #
    #     if not check:
    #         if len(socket_list) == hole_number:
    #             heapq.heapify(socket_list)
    #             heapq.heappop(socket_list)
    #             num += 1
    #
    #         for socket in range(len(socket_list)):
    #             if socket_list[socket][0] + 1 > 0:
    #                 socket_list[socket] = (-999999, socket_list[socket][1])
    #             else:
    #                 socket_list[socket] = (socket_list[socket][0] + 1, socket_list[socket][1])
    #         heapq.heappush(socket_list, (-power_socket_distance[pop_index], use_list[pop_index]))
    #
    # print(num)
    #   ===========================================================================
    #
    # while deque_:
    #     popleft = deque_.popleft()
    #     check = False
    #     # 소켓 전부 1씩 거리 마이너스
    #     for x in range(len(socket_list)):
    #         socket_list[x][0] += 1
    #
    #     for x in range(len(socket_list)):
    #         # 같은거 찾은 (소켓에 꼽혀있음)
    #         if socket_list[x][1] == popleft:
    #             socket_list[x][0] = -power_socket_distance[socket_list[x][0] + index]
    #             check = True
    #             continue
    #     # 같은거 못찾음
    #     if not check:
    #         # 근데 소켓이 다찼음
    #         if len(socket_list) == hole_number:
    #             heapq.heappop(socket_list) # 거리가 가장 먼 소켓 뽑고
    #             num += 1
    #             heapq.heappush(socket_list, [-power_socket_distance[index], popleft]) # 현재껄로 끼우고
    #         else:
    #             # 소켓이 비워져있음
    #             heapq.heappush(socket_list, [-power_socket_distance[popleft], popleft]) # 현재껄로 끼우고
    # print(num)
