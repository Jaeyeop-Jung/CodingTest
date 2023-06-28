# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# dR = [0, 1, 0, -1]
# dC = [1, 0, -1, 0]
#
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# def inRange(r, c):
#     if not 0 <= r < n or not 0 <= c < m:
#         return False
#     return True
#
# def isInside(r, c):
#     visited = [[False] * m for _ in range(n)]
#     visited[r][c] = True
#     q = deque([[r, c]])
#     while q:
#         curR, curC, = q.popleft()
#         for i in range(4):
#             movedR, movedC = curR + dR[i], curC + dC[i]
#             if inRange(movedR, movedC) and not visited[movedR][movedC] and arr[movedR][movedC] == 0:
#                 visited[movedR][movedC] = True
#                 q.append([movedR, movedC])
#             elif not inRange(movedR, movedC):
#                 return False
#     return True
#
# def melt():
#     newArr = [i[:] for i in arr]
#     cnt = 0
#     for r in range(n):
#         for c in range(m):
#             if arr[r][c] == 0:
#                 continue
#             airCnt = 0
#             for i in range(4):
#                 movedR, movedC = r + dR[i], c + dC[i]
#                 if arr[movedR][movedC] == 0 and not isInside(movedR, movedC):
#                     airCnt += 1
#             if 2 <= airCnt and not isInside(r, c):
#                 cnt += 1
#                 newArr[r][c] = 0
#     return newArr, cnt == 0
#
#
# for second in range(sys.maxsize):
#     arr, notMelt = melt()
#     if notMelt:
#         print(second)
#         break

import sys
from collections import deque

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < m:
        return False
    return True

def isInside():
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque([[0, 0]])
    while q:
        curR, curC, = q.popleft()
        for i in range(4):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if inRange(movedR, movedC) and not visited[movedR][movedC]:
                if arr[movedR][movedC] == 0:
                    q.append([movedR, movedC])
                visited[movedR][movedC] = True
    return visited

def melt():
    newArr = [i[:] for i in arr]
    cnt = 0
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 0 or not inside[r][c]:
                continue

            airCnt = 0
            for i in range(4):
                movedR, movedC = r + dR[i], c + dC[i]
                if arr[movedR][movedC] == 0 and inside[movedR][movedC]:
                    airCnt += 1
            if 2 <= airCnt:
                cnt += 1
                newArr[r][c] = 0

    return newArr, cnt == 0


for second in range(sys.maxsize):
    inside = isInside()
    arr, notMelt = melt()
    if notMelt:
        print(second)
        break
