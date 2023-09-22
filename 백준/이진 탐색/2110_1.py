# TODO 틀림

# import math
# from bisect import bisect_left
# from collections import deque
#
# n, m = map(int, input().split())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# arr.sort()
#
# if m == 2:
#     print(arr[-1] - arr[0])
# else:
#     result = math.inf
#     q = deque()
#     q.append([0, len(arr) - 1])
#     cnt = 2
#     while q and cnt < m:
#         start, end, = q.popleft()
#         mid = (arr[start] + arr[end]) // 2
#         if arr[(start + end) // 2] == mid:
#             mid = (start + end) // 2
#         elif bisect_left(arr, mid) == 0 or bisect_left(arr, mid) == len(arr) - 1:
#             mid = bisect_left(arr, mid)
#         else:
#             mid = bisect_left(arr, mid) - 1
#         q.append([start, mid])
#         q.append([mid, end])
#         result = min(result, arr[mid] - arr[start], arr[end] - arr[mid])
#         if result == 1:
#             print(result)
#             break
#         cnt += 1
#     else:
#         print(result)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

def isAvailable(diff):
    idx = 1
    preValue = arr[0]
    cnt = 1
    while idx < len(arr) and cnt < m:
        if diff <= arr[idx] - preValue:
            preValue = arr[idx]
            cnt += 1
            idx += 1
        else:
            idx += 1
    if cnt == m:
        return True
    return False

start = 1
end = arr[-1] - arr[0]
while start <= end:
    mid = (start + end) // 2
    if isAvailable(mid):
        start = mid + 1
    else:
        end = mid - 1
print(start - 1)
