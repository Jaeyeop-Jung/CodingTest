# TODO 틀림 풀 수 있다 잘 생각해봐

# import sys
# import heapq
# input = sys.stdin.readline
#
# n, k, = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# bags = [int(input()) for _ in range(k)]
# arr.sort(key=lambda x: x[0])
# bags.sort()
#
# result = 0
# for bag in bags:
#     h = []
#     totalValue = 0
#     totalWeight = 0
#     for i in range(len(arr)):
#         if arr[i][0] <= bag:
#             if arr[i][0] + totalWeight <= bag:
#                 heapq.heappush(h, [arr[i][1], arr[i][0], i])
#                 totalWeight += arr[i][0]
#                 totalValue += arr[i][1]
#                 continue
#             tempTotal = totalValue
#             tempWeight = totalWeight
#             tempH = h[:]
#             while tempH:
#                 v, w, _, = heapq.heappop(tempH)
#                 tempTotal -= v
#                 tempWeight -= w
#                 if tempWeight + arr[i][0] <= bag:
#                     break
#             tempTotal += arr[i][1]
#             tempWeight += arr[i][0]
#             heapq.heappush(tempH, [arr[i][1], arr[i][0], i])
#             if totalValue < tempTotal:
#                 h = tempH
#                 totalValue = tempTotal
#                 totalWeight = tempWeight
#         else:
#             break
#     h.sort(key=lambda x: x[2])
#     while h:
#         _, _, i, = h.pop()
#         arr.pop(i)
#     result += totalValue
#
# print(result)

# import sys
# import heapq
# input = sys.stdin.readline
#
# n, k, = map(int, input().split())
# h = []
# for _ in range(n):
#     w, v = map(int, input().split())
#     heapq.heappush(h, [-v, w])
# bags = [int(input()) for _ in range(k)]
# bags.sort()
#
# result = 0
# for bag in bags:
#     tempH = []
#     while h:
#         v, w, = heapq.heappop(h)
#         if w <= bag:
#             result += -v
#             break
#         else:
#             heapq.heappush(tempH, [v, w])
#     h = tempH + h
#
# print(result)

import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
bag = []

for i in range(n):
    heapq.heappush(arr, tuple(map(int, input().split())))
for i in range(k):
    bag.append(int(input()))
bag.sort()

result = 0
temp = []
for b in bag:
    while arr and b >= arr[0][0]:
        heapq.heappush(temp, -heapq.heappop(arr)[1])
    if temp:
        result -= heapq.heappop(temp)
    elif not arr:
        break
print(result)