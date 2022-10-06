import sys
import heapq


# 모듈 사용 매우 간단!!!!!
# if __name__ == '__main__':
#     count = int(sys.stdin.readline().rstrip())
#
#     heap = []
#
#
#     for i in range(count):
#         number = int(sys.stdin.readline().rstrip())
#
#         if number != 0:
#             heapq.heappush(heap,(-number,number))
#         else:
#             if len(heap) == 0 :
#                 print(0)
#             else:
#                 print(heapq.heappop(heap)[1])


# 직접 구현
def heap_sort(heap):
    def up_heap(heap, left, right):

        temp = heap[left]

        parent = left

        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1

            child = cr if cr > right and heap[cr] <= heap[cl] else cl

            if temp >= heap[child]:
                break
            heap[parent] = heap[child]
            parent = child
        heap[parent] = temp

    n = len(heap)

    for i in range((n - 1) // 2, -1, -1):
        up_heap(heap, i, n - 1)

    for j in range(n - 1, 0, -1):
        heap[0], heap[j] = heap[j], heap[0]
        up_heap(heap, 0, j - 1)


if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())

    heap = []

    for i in range(count):
        number = int(sys.stdin.readline().rstrip())

        if number != 0:
            heap.append(number)
            heap_sort(heap)
        else:
            if len(heap) == 0:
                print(0)
            else:
                print(heap[0])
                del heap[0]
                heap_sort(heap)
