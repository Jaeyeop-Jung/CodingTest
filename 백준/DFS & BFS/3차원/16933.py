# TODO 틀림 다음엔 맞을 수 있을거다

# import math
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# dR = [0, 1, 0, -1]
# dC = [1, 0, -1, 0]
# afternoon = 0
# night = 1
#
# n, m, k, = map(int, input().split())
# arr = [list(map(int, list(input().strip()))) for _ in range(n)]
#
# if n == m == 1:
#     print(1)
#     exit()
#
# visited = [[[math.inf for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
# visited[0][0][0] = 1
# q = deque()
# q.append([0, 0, 2, afternoon, 0])
#
# while q:
#     r, c, cost, day, broken = q.popleft()
#     for i in range(4):
#         movedR, movedC = r + dR[i], c + dC[i]
#         nextDay = day ^ 1
#         if not 0 <= movedR < n or not 0 <= movedC < m:
#             continue
#         if movedR == n - 1 and movedC == m - 1:
#             print(cost)
#             exit()
#
#         if arr[movedR][movedC] == 1:
#             if day == afternoon and broken < k and cost < visited[movedR][movedC][broken + 1]:
#                 q.append([movedR, movedC, cost + 1, nextDay, broken + 1])
#                 visited[movedR][movedC][broken + 1] = cost
#             else:
#                 q.append([r, c, cost + 1, nextDay, broken])
#         else:
#             if cost < visited[movedR][movedC][broken]:
#                 visited[movedR][movedC][broken] = cost
#                 q.append([movedR, movedC, cost + 1, nextDay, broken])
#
#
#
#         # if arr[movedR][movedC] == 0:
#         #     if cost < visited[movedR][movedC][broken]:
#         #         visited[movedR][movedC][broken] = cost
#         #         q.append([movedR, movedC, cost + 1, nextDay, broken])
#         # else:
#         #     if broken < k and cost < visited[movedR][movedC][broken + 1]:
#         #         visited[movedR][movedC][broken + 1] = cost
#         #         q.append([movedR, movedC, cost + 1, nextDay, broken + 1])
#         # if arr[movedR][movedC] == 1:
#         #     continue
#         # if cost < visited[movedR][movedC][broken]:
#         #     visited[movedR][movedC][broken] = cost
#         #     q.append([movedR, movedC, cost + 1, nextDay, broken])
#
# print(-1)

import math
import sys
from collections import deque

input = sys.stdin.readline

dR = [0, 1, 0, -1, 0]
dC = [1, 0, -1, 0, 0]
afternoon = 0
night = 1

n, m, k, = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

visited = [[[[math.inf] * (k + 1) for _ in range(2)] for _ in range(m)] for _ in range(n)]
visited[0][0][afternoon][0] = 1
q = deque()
q.append([0, 0, 2, afternoon, 0])

while q:
    r, c, cost, day, broken = q.popleft()
    for i in range(5):
        movedR, movedC = r + dR[i], c + dC[i]
        nextDay = day ^ 1
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if movedR == n - 1 and movedC == m - 1:
            print(cost)
            exit()

        if arr[movedR][movedC] == 1:
            if day == afternoon and broken < k and cost < visited[movedR][movedC][nextDay][broken + 1]:
                q.append([movedR, movedC, cost + 1, nextDay, broken + 1])
                visited[movedR][movedC][nextDay][broken + 1] = cost
            elif day == night:
                if cost < visited[r][c][nextDay][broken]:
                    q.append([r, c, cost + 1, nextDay, broken])
                    visited[r][c][nextDay][broken] = cost
        else:
            if cost < visited[movedR][movedC][nextDay][broken]:
                visited[movedR][movedC][nextDay][broken] = cost
                q.append([movedR, movedC, cost + 1, nextDay, broken])

print(-1)