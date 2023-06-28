# import sys
#
# input = sys.stdin.readline
#
# dR = [0, 1, 0, -1]
# dC = [1, 0, -1, 0]
#
# m, n = map(int, input().split())
#
# add = [0] * (2 * m - 1)
# for _ in range(n):
#     zero, one, two = map(int, input().split())
#     for i in range(2 * m - 1):
#         if 0 < zero:
#             zero -= 1
#         elif 0 < one:
#             one -= 1
#             add[i] += 1
#         else:
#             two -= 1
#             add[i] += 2
#
# arr = [[0] * m for _ in range(m)]
# idx = 0
# for r in range(m - 1, -1, -1):
#     arr[r][0] += add[idx]
#     idx += 1
# for c in range(1, m):
#     arr[0][c] += add[idx]
#     idx += 1
#
# for r in range(1, m):
#     for c in range(1, m):
#         arr[r][c] = max(arr[r - 1][c], arr[r - 1][c - 1], arr[r][c - 1])
#
# for r in range(m):
#     for c in range(m):
#         print(arr[r][c] + 1, end=' ')
#     print()

import sys

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

m, n = map(int, input().split())

add = [0] * 3
for _ in range(n):
    zero, one, two = map(int, input().split())
    add[0] += zero
    add[1] += one
    add[2] += two

arr = [[0] * m for _ in range(m)]
temp = []
temp.append(add[0] // (2 * m - 1))
add[0] %= 2 * m - 1
temp.append((add[0] + add[1]) // (2 * m - 1))
add[1] %= 2 * m - 1
temp.append(add[0] // (2 * m - 1))
add[0] %= 2 * m - 1

for r in range(1, m):
    for c in range(1, m):
        arr[r][c] = max(arr[r - 1][c], arr[r - 1][c - 1], arr[r][c - 1])

for r in range(m):
    for c in range(m):
        print(arr[r][c] + 1, end=' ')
    print()