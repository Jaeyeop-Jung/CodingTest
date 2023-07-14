# import sys
#
# input = sys.stdin.readline
#
# dR = [0, 1, 0, -1]
# dC = [1, 0, -1, 0]
#
# n, k, = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# second, r, c = map(int, input().split())
#
# def spread(arr):
#     newArr = [i[:] for i in arr]
#     for r in range(n):
#         for c in range(n):
#             if arr[r][c] != 0:
#                 for d in range(4):
#                     movedR, movedC = r + dR[d], c + dC[d]
#                     if not 0 <= movedR < n or not 0 <= movedC < n:
#                         continue
#                     if arr[movedR][movedC] == 0:
#                         if newArr[movedR][movedC] == 0:
#                             newArr[movedR][movedC] = arr[r][c]
#                         else:
#                             newArr[movedR][movedC] = max(newArr[movedR][movedC], arr[r][c])
#     return newArr
#
# for _ in range(second):
#     arr = spread(arr)
#
# print(arr[r - 1][c - 1])

import sys
from collections import deque

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, k, = map(int, input().split())
arr = []
q = []
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(n):
        if temp[c] != 0:
            q.append([temp[c], r, c, 0])
    arr.append(temp)
second, r, c = map(int, input().split())

q = deque(sorted(q))
while q:
    num, curR, curC, sec = q.popleft()
    if curR == r - 1 and curC == c - 1:
        if sec <= second:
            print(num)
        else:
            print(0)
        exit()
    for i in range(4):
        movedR, movedC = curR + dR[i], curC + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < n:
            continue
        if arr[movedR][movedC] != 0:
            continue
        arr[movedR][movedC] = num
        q.append([num, movedR, movedC, sec + 1])
