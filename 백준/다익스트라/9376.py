# TODO 틀림

# import math
# import heapq
#
# dRow = [0, 1, 0, -1]
# dColumn = [1, 0, -1, 0]
#
# def dijkstra(r, c):
#     rout = []
#     distance = [[math.inf] * w for _ in range(h)]
#     heap = []
#     if board[r][c] == '#':
#         heapq.heappush(heap, [r, c, 1, [[r, c]]])
#         distance[r][c] = 1
#     if board[r][c] == '.':
#         heapq.heappush(heap, [r, c, 0, [[r, c]]])
#         distance[r][c] = 0
#
#     while heap:
#         curR, curC, cnt, route = heapq.heappop(heap)
#         if distance[curR][curC] < cnt:
#             continue
#         for i in range(len(dRow)):
#             nextR = curR + dRow[i]
#             nextC = curC + dColumn[i]
#             nextCnt = cnt
#             if not 0 <= nextR < h or not 0 <= nextC < w:
#                 continue
#             if board[nextR][nextC] == '*':
#                 continue
#             elif board[nextR][nextC] == '#':
#                 nextCnt += 1
#             if nextCnt < distance[nextR][nextC]:
#                 distance[nextR][nextC] = nextCnt
#                 newRoute = route[:]
#                 newRoute.append([nextR, nextC])
#                 if board[nextR][nextC] == '$':
#                     rout.append(newRoute)
#                 heapq.heappush(heap, [nextR, nextC, nextCnt, newRoute])
#     idx = 0
#     while idx < len(rout):
#         finalR, finalC, = rout[idx][-1]
#         if board[finalR][finalC] != '$':
#             rout.pop(idx)
#             continue
#         idx += 1
#
#     return 1
#
# t = int(input())
# for _ in range(t):
#     h, w, = map(int, input().split())
#     board = []
#     for i in range(h):
#         board.append(input())
#     start = []
#     for i in range(h):
#         if i == 0:
#             for j in range(w):
#                 if board[i][j] == '#' or board[i][j] == '.':
#                     start.append([i, j])
#         elif i == h - 1:
#             for j in range(w):
#                 if board[i][j] == '#' or board[i][j] == '.':
#                     start.append([i, j])
#         else:
#             for r in range(1, h - 1):
#                 if board[r][0] == '#' or board[r][0] == '.':
#                     start.append([r, 0])
#                 if board[r][-1] == '#' or board[r][-1] == '.':
#                     start.append([r, w - 1])
#
#     result = math.inf
#     for i in range(len(start)):
#         result = min(result, dijkstra(start[i][0], start[i][1]))
import math
from collections import deque

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]


def bfs(r, c):
    map = [[math.inf] * (w + 2) for _ in range(h + 2)]
    q = deque()
    q.append([r, c, 0])
    map[r][c] = 0

    while q:
        row, column, cnt = q.popleft()
        map[row][column] = min(map[row][column], cnt)
        for i in range(len(dRow)):
            movedR = row + dRow[i]
            movedC = column + dColumn[i]
            if not 0 <= movedR < h + 2 or not 0 <= movedC < w + 2:
                continue
            if board[movedR][movedC] == '*':
                continue
            elif cnt < map[movedR][movedC] and (board[movedR][movedC] == '.' or board[movedR][movedC] == '$'):
                q.appendleft([movedR, movedC, cnt])
                map[movedR][movedC] = cnt
            elif cnt + 1 < map[movedR][movedC] and board[movedR][movedC] == '#':
                q.append([movedR, movedC, cnt + 1])
                map[movedR][movedC] = cnt + 1
    return map

t = int(input())
for _ in range(t):
    h, w, = map(int, input().split())
    board = []
    board.append('.' * (w + 2))
    for _ in range(h):
        board.append('.' + input() + '.')
    board.append('.' * (w + 2))

    d1 = []
    d2 = []
    for i in range(1, len(board) - 1):
        for j in range(1, len(board[i]) - 1):
            if board[i][j] == '$':
                if not d1:
                    d1 = [i, j]
                else:
                    d2 = [i, j]

    map1 = bfs(d1[0], d1[1])
    map2 = bfs(d2[0], d2[1])
    map3 = bfs(0, 0)

    result = math.inf
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            if map1[i][j] == math.inf or map2[i][j] == math.inf or map3[i][j] == math.inf:
                continue
            if board[i][j] == '#':
                result = min(result, map1[i][j] + map2[i][j] + map3[i][j] - 2)
            else:
                result = min(result, map1[i][j] + map2[i][j] + map3[i][j])
    print(result)