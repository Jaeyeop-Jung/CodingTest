# TODO 틀림 은근 어렵다

import sys

input = sys.stdin.readline

n = int(input())
arr = sorted([[i, int(input()), 0] for i in range(n)], key=lambda x: x[1])

while 17 < abs(arr[-1][1] - arr[0][1]):
    left_end, right_end = 0, n - 1
    leftCost = 0
    for i in range(len(arr)):
        if arr[i][1] == arr[left_end][1]:
            leftCost += (arr[i][2] + 1) ** 2
            left_end = i
        else:
            break
    rightCost = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i][1] == arr[right_end][1]:
            rightCost += (arr[i][2] + 1) ** 2
            right_end = i
        else:
            break

    if leftCost < rightCost:
        for i in range(left_end + 1):
            arr[i][1] += 1
            arr[i][2] += 1
    else:
        for i in range(len(arr) - 1, right_end - 1, -1):
            arr[i][1] -= 1
            arr[i][2] += 1

print(sum([arr[i][2] ** 2 for i in range(len(arr))]))
