# TODO 맞긴 했는데 이분탐색으로 생각하는 법도 찾아야된다

import math

n, m, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# cur = 0
# diff = []
# for i in range(n):
#     diff.append(arr[i] - cur)
#     cur = arr[i]
# diff.append(l - cur)
#
# install = [1] * (n + 1)
# newDiff = diff[:]
#
# for _ in range(m):
#     maxDiff = max(newDiff)
#     idx = newDiff.index(maxDiff)
#     if maxDiff % (install[idx] + 1) == 0:
#         install[idx] += 1
#         newDiff[idx] = diff[idx] // install[idx]
#     else:
#         install[idx] += 1
#         newDiff[idx] = math.ceil(diff[idx] / install[idx])
#
# print(max(newDiff))

arr = [0] + arr + [l]
left, right = 1, l - 1
res = 0
while left <= right:
    mid = (left + right) // 2
    temp = 0
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        if mid < diff:
            if diff % mid == 0:
                temp += diff // mid - 1
            else:
                temp += diff // mid
    if temp <= m:
        right = mid - 1
        res = mid
    else:
        left = mid + 1

print(res)