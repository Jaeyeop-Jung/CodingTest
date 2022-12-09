# TODO 틀림 아이디어는 맞았는데 구현을 잘 해봐 맞을 수 있다

import sys
input = sys.stdin.readline

dic = {
    0: 5,
    1: 4,
    2: 3,
    3: 2,
    4: 1,
    5: 0
}

def getMin(size):
    min_lists = []
    min_lists.append(min(arr[0], arr[5]))
    min_lists.append(min(arr[1], arr[4]))
    min_lists.append(min(arr[2], arr[3]))
    min_lists.sort()
    return sum(min_lists[:size])

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(sum(arr) - max(arr))
# elif n == 2:
#     print(getMin(2) * 4 + getMin(3) * 4)
else:
    print(
        (getMin(2) * 4 + getMin(1) * (n - 2) * 4) * (n - 1)
        + getMin(3) * 4 + getMin(2) * (n - 2) * 4 + getMin(1) * (n - 2) ** 2
    )