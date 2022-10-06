import sys

#
# if __name__ == '__main__':
#     string_list = list(sys.stdin.readline().rstrip())
#
#     f_check = 0
#     s_check = 0
#
#     f_l_count = 0
#     f_r_count = 0
#
#     s_l_count = 0
#     s_r_count = 0
#
#     answer_list = ["0"]
#     open_list = []
#     sign_list = []
#
#     for i in range(len(string_list)):
#         pop_s = string_list.pop()
#
#         if pop_s == ")":
#             f_check += 1
#             f_r_count += 1
#             if len(open_list) > 0:
#                 answer_list.append("*")
#             else:
#                 answer_list.append("+")
#             open_list.append(2)
#             answer_list.append("2")
#         elif pop_s == "(":
#             if f_check <= 0:
#                 print(0)
#                 break
#             else:
#                 f_check -= 1
#                 f_l_count += 1
#                 open_list.pop()
#
#         elif pop_s == "]":
#             s_check += 1
#             s_r_count += 1
#             if len(open_list) > 0:
#                 answer_list.append("*")
#             else:
#                 answer_list.append("+")
#             open_list.append(3)
#             answer_list.append("3")
#         elif pop_s == "[":
#             if s_check <= 0:
#                 print(0)
#                 break
#             else:
#                 s_check -= 1
#                 s_l_count += 1
#                 open_list.pop()
#
#
#     if f_l_count != f_r_count:
#         print(0)
#     if s_l_count != s_r_count:
#         print(0)
#
#
#     print(answer_list)
#     print("".join(answer_list))
#     print(int(str(answer_list)))


if __name__ == '__main__':
    string_list = list(sys.stdin.readline().rstrip())

    depth = 0

    f_check = 0
    s_check = 0

    f_l_count = 0
    f_r_count = 0

    s_l_count = 0
    s_r_count = 0

    answer_list = []
    present = 1

    for i in range(len(string_list)):
        pop_s = string_list.pop()

        if pop_s == ")":
            f_check += 1
            f_r_count += 1
            present *= 2

            if len(string_list) >= 1 :
                if string_list[len(string_list)-1] == "(":
                    answer_list.append(present)

        elif pop_s == "(":
            if f_check <= 0:
                answer_list.clear()
                break
            else:
                f_check -= 1
                f_l_count += 1

                present //=2

        elif pop_s == "]":
            s_check += 1
            s_r_count += 1
            present *=3
            if len(string_list) >= 1 :
                if string_list[len(string_list)-1] == "[":
                    answer_list.append(present)

        elif pop_s == "[":
            if s_check <= 0:
                answer_list.clear()
                break
            else:
                s_check -= 1
                s_l_count += 1
                present //=3


    if f_l_count != f_r_count:
        print(0)
    elif s_l_count != s_r_count:
        print(0)
    else:
        print(sum(answer_list))


