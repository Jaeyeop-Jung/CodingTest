# TODO 틀림 잘 고민해봐 맞아야지

# import sys
# from collections import defaultdict, deque
#
# input = sys.stdin.readline
#
# dR = [0, 1, 0, -1]
# dC = [1, 0, -1, 0]
#
# n, m, = map(int, input().split())
# graph = defaultdict(list)
# for _ in range(m):
#     x, y, a, b = map(int, input().split())
#     graph[(x - 1, y - 1)].append((a - 1, b - 1))
#
# visited = [[False] * n for _ in range(n)]
# visited[0][0] = True
# q = deque()
# q.append((0, 0))
# light = [[False] * n for _ in range(n)]
# light[0][0] = True
# while q:
#     r, c, = q.popleft()
#     for nextR, nextC in graph[(r, c)]:
#         if not light[nextR][nextC]:
#             light[nextR][nextC] = True
#             for i in range(4):
#                 movedR, movedC = nextR + dR[i], nextC + dC[i]
#                 if not 0 <= movedR < n or not 0 <= movedC < n:
#                     continue
#                 if visited[movedR][movedC]:
#                     q.append((nextR, nextC))
#
#     for i in range(4):
#         movedR, movedC = r + dR[i], c + dC[i]
#         if not 0 <= movedR < n or not 0 <= movedC < n:
#             continue
#         if not visited[movedR][movedC] and light[movedR][movedC]:
#             q.append((movedR, movedC))
#             visited[movedR][movedC] = True
#
# print(sum([i.count(True) for i in light]))


import sys
from collections import defaultdict, deque

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    x, y, a, b = map(int, input().split())
    graph[(x - 1, y - 1)].append((a - 1, b - 1))

visited = [[False] * n for _ in range(n)]
visited[0][0] = True
q = deque()
light = [[False] * n for _ in range(n)]
light[0][0] = True
q.append((0, 0))
while q:
    r, c, = q.popleft()
    # 불 밝히고
    # 가고
    for nR, nC in graph[(r, c)]:
        light[nR][nC] = True
        for i in range(4):
            movedR, movedC = nR + dR[i], nC + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if visited[movedR][movedC] and not visited[nR][nC]:
                q.append((nR, nC))
                visited[nR][nC] = True

    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < n:
            continue
        if light[movedR][movedC] and not visited[movedR][movedC]:
            q.append((movedR, movedC))
            visited[movedR][movedC] = True

print(sum([i.count(True) for i in light]))