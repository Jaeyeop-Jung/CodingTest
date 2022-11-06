import math
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

dRow = [0, 1, 1, 1, 0, -1, -1, -1]
dColumn = [1, 1, 0, -1, -1, -1, 0, 1]

result = math.inf

# def dfs(worldmap, visited, r, c, direction, cnt):
#     if r == len(worldmap) - 1 and c == len(worldmap[-1]) - 1:
#         global result
#         result = min(result, cnt)
#
#     visited[r][c] = True
#     for i in [-1, 0, 1]:
#         movedDirection = direction + i
#         if movedDirection == -1:
#             movedDirection = len(dRow) - 1
#         elif movedDirection == len(dRow):
#             movedDirection = 0
#
#         # 대각선 X
#         if movedDirection % 2 == 0:
#             movedR = r + dRow[movedDirection]
#             movedC = c + dColumn[movedDirection]
#             if not 0 <= movedR < len(worldmap) or not 0 <= movedC < len(worldmap[0]):
#                 continue
#             if visited[movedR][movedC] or worldmap[movedR][movedC] == 'X':
#                 continue
#             dfs(worldmap, visited, movedR, movedC, movedDirection, cnt + 1)
#             visited[movedR][movedC] = False
#
#         # 대각선 O
#         else:
#             movedR = r + dRow[movedDirection]
#             movedC = c + dColumn[movedDirection]
#             if not 0 <= movedR < len(worldmap) or not 0 <= movedC < len(worldmap[0]):
#                 continue
#             if visited[movedR][movedC] or worldmap[movedR][movedC] == 'X':
#                 continue
#             if worldmap[movedR - 1][movedC] == 'X' or worldmap[movedR][movedC - 1] == 'X':
#                 continue
#             dfs(worldmap, visited, movedR, movedC, movedDirection, cnt + 1)
#             visited[movedR][movedC] = False
#
# def solution(worldmap):
#     dfs(worldmap, [[False] * len(worldmap[i]) for i in range(len(worldmap))], 0, 0, 0, 0)
#     return result

def solution(worldmap):
    result = math.inf
    q = deque()
    visited = [[False] * len(worldmap[i]) for i in range(len(worldmap))]
    q.append([0, 0, 0, 0])

    while q:
        r, c, d, cnt = q.popleft()
        visited[r][c] = True

        if r == len(worldmap) - 1 and c == len(worldmap[-1]) -1:
            result = min(result, cnt)

        for i in [-1, 0, 1]:
            movedD = d + i
            if movedD == -1:
                movedD = len(dRow) - 1
            elif movedD == len(dRow):
                movedD = 0

            # 대각선 X
            if movedD % 2 == 0:
                movedR = r + dRow[movedD]
                movedC = c + dColumn[movedD]
                if not 0 <= movedR < len(worldmap) or not 0 <= movedC < len(worldmap[0]):
                    continue
                if visited[movedR][movedC] or worldmap[movedR][movedC] == 'X':
                    continue
                q.append([movedR, movedC, movedD, cnt + 1])
                visited[movedR][movedC] = True

            # 대각선 O
            else:
                movedR = r + dRow[movedD]
                movedC = c + dColumn[movedD]
                if not 0 <= movedR < len(worldmap) or not 0 <= movedC < len(worldmap[0]):
                    continue
                if visited[movedR][movedC] or worldmap[movedR][movedC] == 'X':
                    continue
                if worldmap[movedR - 1][movedC] == 'X' or worldmap[movedR][movedC - 1] == 'X':
                    continue
                q.append([movedR, movedC, movedD, cnt + 1])
                visited[movedR - 1][movedC] = True
                visited[movedR][movedC - 1] = True
                visited[movedR][movedC] = True

    return result


print(solution(["..XXX", "..XXX", "...XX", "X....", "XXX.."]))