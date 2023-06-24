# TODO 풀긴했는데 정해는 아니다. 잘 생각해봐

# import sys
# import heapq
# from collections import defaultdict
#
# input = sys.stdin.readline
#
# n = int(input())
# h = []
# for _ in range(n):
#     p, d = map(int, input().split())
#     heapq.heappush(h, [-p, d])
#
#
# heapq.heapify(h)
# res = 0
#
# def isAvailable():
#     if not temp:
#         return True
#
#     cnt = 0
#     for day in temp:
#         if day <= d:
#             cnt += len(temp[day])
#
#     if cnt < d:
#         return True
#
#     return False
#
# temp = defaultdict(list)
# while h:
#     p, d, = heapq.heappop(h)
#
#     if not isAvailable():
#         continue
#
#     temp[d].append(p)
#
# for d in temp:
#     for p in temp[d]:
#         res += -p
#
# print(res)

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (-x[0]))

days = [False] * 10_001
res = 0
for p, d in arr:
    for curD in range(d, 0, -1):
        if not days[curD]:
            res += p
            days[curD] = True
            break

print(res)