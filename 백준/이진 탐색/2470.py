# TODO 틀림  https://velog.io/@kcs05008/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%91%90-%EC%9A%A9%EC%95%A1-%EB%B0%B1%EC%A4%80-2470-python

# import math
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# arr.sort()
# result = [math.inf, [0, 0]]
# for i in range(len(arr)):
#     temp = [[arr[j] - arr[i], [i, j]] for j in range(len(arr)) if i != j]
#     temp.sort(key=lambda x: x[0])
#     start = 0
#     end = len(temp) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if temp[mid][0] == 0:
#             result = temp[mid]
#             break
#         else:
#             if result[0] != math.inf and abs(temp[mid][0]) < abs(temp[result[0]][0]):
#                 result = temp[mid]
#                 end = mid - 1
#             else:
#                 start = mid + 1
# print(arr)

import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

start = 0
end = n-1
czero = abs(arr[start]+arr[end])
cstart = start
cend = end

while start<end:
    tmp = arr[start]+arr[end]
    if abs(tmp) < czero:
        cstart = start
        cend = end
        czero = abs(tmp)
        if czero == 0:
            break
    if tmp > 0:
        end -= 1
    else:
        start += 1

print(arr[cstart], arr[cend])
