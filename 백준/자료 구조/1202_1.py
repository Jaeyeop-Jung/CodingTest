# TODO 틀림 다음엔 맞자 우연하게 생각해봐

import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

bags.sort(reverse=True)
h = []
for m, v in arr:
    heapq.heappush(h, [m, v])
res = 0
temp = []
while bags:
    bag = bags.pop()
    while h and h[0][0] <= bag:
        heapq.heappush(temp, -heapq.heappop(h)[1])
    res -= heapq.heappop(temp)

print(res)

# import heapq
# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# arr = []
# bag = []
#
# for i in range(n):
#     heapq.heappush(arr, tuple(map(int, input().split())))
# for i in range(k):
#     bag.append(int(input()))
# bag.sort()
#
# result = 0
# temp = []
# for b in bag:
#     while arr and b >= arr[0][0]:
#         heapq.heappush(temp, -heapq.heappop(arr)[1])
#     if temp:
#         result -= heapq.heappop(temp)
#     elif not arr:
#         break
# print(result)