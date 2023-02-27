# TODO 틀림 잘 생각해봐라...

# import math
#
# n = int(input())
# stack = [[] for _ in range(n)]
# cur = 0
# for r in range(n):
#     temp = list(map(int, input().split()))
#     for c in range(n):
#         stack[c].append(temp[c])
#
# cnt = 0
# while True:
#     if cnt == n:
#         print(cur)
#         exit()
#
#     diff = math.inf
#     idx = -1
#     for c in range(n):
#         if cur - stack[c][-1] < diff:
#             diff = cur - stack[c][-1]
#             idx = c
#
#     cur = stack[idx].pop()
#     cnt += 1

import heapq

n = int(input())
h = []
for r in range(n):
    for i in map(int, input().split()):
        heapq.heappush(h, -i)

for i in range(n - 1):
    heapq.heappop(h)

print(-heapq.heappop(h))