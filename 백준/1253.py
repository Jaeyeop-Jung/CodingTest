# TODO 틀림

# import sys
# from collections import defaultdict
# from collections import Counter
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# zero = 0
# for i in range(n - 1, -1, -1):
#     if arr[i] == 0:
#         arr.pop(i)
#         zero += 1
#
# n = len(arr)
# dic = defaultdict(int)
# for i in range(n):
#     for j in range(i + 1, n):
#         dic[arr[i] + arr[j]] += 1
#
# counter = dict(Counter(arr))
# res = 0
# for key in dic:
#     if key in counter:
#         res += counter[key]
#
# if 1 <= zero:
#     temp = 0
#     for key in counter:
#         if 2 <= counter[key]:
#             temp += ((counter[key] - 1) * counter[key]) * zero
#     if 2 <= zero:
#         temp += (zero * (zero - 1)) // 2
#     res += temp // 2
#
# print(res)

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
res = 0
for left in range(n):
    for right in range(left + 1, n):
        target = arr[left] + arr[right]
        leftIdx = max(right, bisect_left(arr, target))
        rightIdx = bisect_right(arr, target) - 1
        if n <= leftIdx:
            continue

        if leftIdx < rightIdx:
            res += rightIdx - leftIdx
        elif leftIdx == rightIdx and arr[leftIdx] == target:
            res += 1
print(res)