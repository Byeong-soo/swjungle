import sys

#
# if __name__ == '__main__':
#     count = int(sys.stdin.readline().rstrip())
#
#     materials = list(map(int, sys.stdin.readline().rstrip().split(" ")))
#     materials.sort()
#
#     result = [0,1]
#     temp_result = [0,1]
#
#     temp_sum = 0
#     start = 0
#     end = 0
#     answer_sum = 1000000000
#
#     for num in range(count):
#         start = num
#
#         if start == count-1:
#             break
#         else:
#             end = start + 1
#         min_sum = materials[num] + materials[end]
#
#         while end <= count - 1:
#             temp_sum = materials[start] + materials[end]
#             if abs(min_sum) < abs(temp_sum):
#                 end -= 1
#                 break
#             elif abs(min_sum) >= abs(temp_sum):
#                 min_sum = temp_sum
#                 temp_result[0] = start
#                 temp_result[1] = end
#
#             if min_sum == 0:
#                 break
#             end += 1
#
#         if abs(answer_sum) > abs(min_sum):
#             answer_sum = min_sum
#             result[0] = temp_result[0]
#             result[1] = temp_result[1]
#
#         if answer_sum == 0:
#             break
#
#     print(materials[result[0]], end=" ")
#     print(materials[result[1]], end="")


if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())
    material_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    material_list.sort()

    start = 0
    end = count - 1
    min_sum = 1000000000000000
    answer = [0, 1]
    while start < end:
        temp_sum = material_list[start] + material_list[end]

        if abs(min_sum) > abs(temp_sum):
            answer[0] = material_list[start]
            answer[1] = material_list[end]
            min_sum = temp_sum

        if temp_sum == 0:
            answer[0] = material_list[start]
            answer[1] = material_list[end]
            break
        elif temp_sum > 0:
            end -= 1
        elif temp_sum < 0:
            start += 1

    print(answer[0],answer[1])
