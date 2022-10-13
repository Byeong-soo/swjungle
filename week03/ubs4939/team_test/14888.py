import sys

def calculate(index,number,plus,minus,mul,div):
    global max_num
    global min_num

    if plus:
        calculate(index+1,number+number_list[index] ,plus-1, minus,mul,div)
    if minus:
        calculate(index+1,number-number_list[index] ,plus, minus-1,mul,div)
    if mul:
        calculate(index+1,number*number_list[index] ,plus, minus,mul-1,div)
    if div:
        calculate(index+1,int(number/number_list[index]) ,plus, minus,mul,div-1)

    if plus ==0 and minus ==0 and mul ==0 and div ==0:

        if number > max_num:
            max_num = number

        if number < min_num:
            min_num = number



if __name__ == '__main__':
    number_count = int(sys.stdin.readline().rstrip())
    number_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    plus, minus, mul, div = map(int, sys.stdin.readline().rstrip().split(" "))

    max_num = float('-inf')
    min_num = float('inf')

    calculate(1,number_list[0],plus,minus,mul,div)
    print(max_num)
    print(min_num)

