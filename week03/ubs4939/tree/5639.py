import sys


def postorder(s, e):
    if s > e:
        return
    mid = e + 1                         # 오른쪽 노드가 없을 경우

    for i in range(s+1, e+1):
        if nums[s] < nums[i]:
            mid = i
            break

    postorder(s+1, mid-1)               # 왼쪽 확인
    postorder(mid, e)                   # 오른쪽 확인
    print(nums[s])


if __name__ == '__main__':

    sys.setrecursionlimit(10**9)
    nums = []
    while True:
        try:
            nums.append(int(sys.stdin.readline()))
        except:
            break

postorder(0, len(nums)-1)