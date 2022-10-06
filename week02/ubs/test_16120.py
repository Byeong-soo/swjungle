import sys

if __name__ == '__main__':
    string_list = list(sys.stdin.readline().rstrip())

    set_count = 0
    string_check = 0

    pop_string_1 = "T"
    pop_string_2 = "T"

    while string_list:

        pop_string_1 = string_list.pop()

        if string_list:
            pop_string_2 = string_list.pop()
        else:
            if set_count == 0 and pop_string_1 == "P":
                print("PPAP")
                break
            else:
                print("NP")
                break
        if pop_string_2 + pop_string_1 == "AP":
            set_count += 1
        elif pop_string_2 + pop_string_1 == "PP":
            if set_count == 0:
                print("NP")
                break
            set_count -= 1
            string_list.append("P")
        else:
            print("NP")
            break
