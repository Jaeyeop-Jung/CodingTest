# TODO 틀림 잘 생각해봐 맞을 수 있다

import sys

input = sys.stdin.readline

n, k, = map(int, input().split())
maximum = 0
minimum = 1000000000
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    maximum = max(maximum, b)
    minimum = min(minimum, a)

board = [0] * (maximum + 2)
for a, b in arr:
    board[a] += 1
    board[b] -= 1

cur = 0
for i in range(minimum, maximum + 1):
    if board[i] != 0:
        cur += board[i]
    board[i] = cur
board = [0] + board
for i in range(1, maximum + 1):
    board[i] = board[i] + board[i - 1]
# def lowerBound(left):
#     start, end = left + 1, maximum
#     minIdx = maximum
#     while start <= end:
#         mid = (start + end) // 2
#         temp = board[mid] - board[left]
#         if k <= temp:
#             end = mid - 1
#             minIdx = min(minIdx, mid)
#         else:
#             start = mid + 1
#     return minIdx
#
# for left in range(minimum, maximum + 1):
#     right = lowerBound(left)
#     if board[right] - board[left] == k:
#         print(left, right)
#         break
# else:
#     print(0, 0)

result = []
left, right = 0, 1
while right <= maximum:
    temp = board[right] - board[left]
    if temp == k:
        result.append([left, right])
        right += 1
    elif temp < k:
        right += 1
    else:
        left += 1

result.sort(key=lambda x: (x[0], x[1]))
if result:
    print(*result[0])
else:
    print(0, 0)


