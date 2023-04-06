# import math
# from collections import deque
#
# dR = [0, 1, 0, -1]
# dC = [1, 0, -1, 0]
#
# n, m, = map(int, input().split())
# arr = []
# virus = []
#
# total = 0
# for r in range(n):
#     temp = list(map(int, input().split()))
#     for c in range(n):
#         if temp[c] == 1:
#             continue
#         if temp[c] == 2:
#             virus.append([r, c])
#         total += 1
#     arr.append(temp)
#
#
# result = math.inf
# def dfs(arr, virus, idx, expose):
#     global result
#     if idx == len(virus) or len(expose) == m:
#         if len(expose) == m:
#             temp = 0
#             for r in range(n):
#                 for c in range(n):
#                     if arr[r][c] == 1 or arr[r][c] == 2:
#                         continue
#                     else:
#                         for i in expose:
#                             temp = max(temp, dp[i][r][c])
#                         if temp == math.inf:
#                             return
#             result = min(result, temp)
#         return
#
#     for i in range(idx, len(virus)):
#         dfs(arr, virus, idx + 1, expose + [i])
#
# dp = []
# for i in range(len(virus)):
#     tempDp = [[math.inf] * n for _ in range(n)]
#     q = deque()
#     r, c = virus[i]
#     q.append([r, c, 0])
#     tempDp[r][c] = 0
#     while q:
#         r, c, cost, = q.popleft()
#         for d in range(4):
#             movedR, movedC = r + dR[d], c + dC[d]
#             if not 0 <= movedR < n or not 0 <= movedC < n or tempDp[movedR][movedC] != math.inf:
#                 continue
#             if arr[movedR][movedC] == 1:
#                 tempDp[movedR][movedC] = -1
#                 continue
#             else:
#                 tempDp[movedR][movedC] = cost + 1
#                 q.append([movedR, movedC, cost + 1])
#     dp.append(tempDp)
#
#
# dfs(arr, virus, 0, [])
# print(result if result != math.inf else -1)


import math
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, = map(int, input().split())
arr = []
virus = []

total = 0
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(n):
        if temp[c] == 1:
            continue
        if temp[c] == 2:
            virus.append([r, c])
        total += 1
    arr.append(temp)


result = math.inf
def dfs(arr, virus, idx, expose):
    global result
    if idx == len(virus) or len(expose) == m:
        # m개 만큼 활성 바이러스를 만들었을 때
        if len(expose) == m:
            visited = [[False] * n for _ in range(n)]
            q = deque()
            cnt = 0
            res = 0
            for exposeIdx in expose:
                r, c = virus[exposeIdx]
                q.append([r, c, 0])
                visited[r][c] = True
                cnt += 1
            while q:
                r, c, cost, = q.popleft()
                for i in range(4):
                    movedR, movedC = r + dR[i], c + dC[i]
                    if not 0 <= movedR < n or not 0 <= movedC < n:
                        continue

                    # 방문 체크
                    if visited[movedR][movedC]:
                        continue

                    # 벽이면 스킵
                    if arr[movedR][movedC] == 1:
                        visited[movedR][movedC] = True
                        continue

                    # 비활성 바이러스 또는 빈 칸이면 값 업데이트 후
                    elif arr[movedR][movedC] == 0:
                        res = max(res, cost + 1)
                    visited[movedR][movedC] = True
                    q.append([movedR, movedC, cost + 1])
                    # 빈 칸을 몇개 채웠는지 확인하기 위해 +1
                    cnt += 1
            # 전체 빈 칸이랑 bfs로 채운 빈 칸이랑 같다면 모두 채웠으니
            if cnt == total:
                result = min(result, res)
        return

    for i in range(idx, len(virus)):
        expose.append(i)
        dfs(arr, virus, i + 1, expose)
        expose.pop()

dfs(arr, virus, 0, [])
print(result if result != math.inf else -1)
