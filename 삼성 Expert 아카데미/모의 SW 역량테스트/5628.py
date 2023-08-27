# import math
# from collections import deque
#
# # dR = [0, 1, 0, -1]
# # dC = [1, 0, -1, 0]
# #
# # def simul(r, c, size):
# #     cnt = 0 if arr[r][c] == 0 else 1
# #     q = deque([[r, c, 1]])
# #     visited = [[False] * n for _ in range(n)]
# #     visited[r][c] = True
# #     while q:
# #         curR, curC, cost, = q.popleft()
# #         for i in range(4):
# #             movedR, movedC = curR + dR[i], curC + dC[i]
# #             if not 0 <= movedR < n or not 0 <= movedC < n:
# #                 continue
# #             if visited[movedR][movedC] or size < cost + 1:
# #                 continue
# #             q.append([movedR, movedC, cost + 1])
# #             visited[movedR][movedC] = True
# #             if arr[movedR][movedC] == 1:
# #                 cnt += 1
# #     if 0 <= cnt * m - (size * size + (size - 1) * (size - 1)):
# #         return cnt
# #     return 0
#
# def simul(r, c, size):
#     cnt = 0
#     for houseR, houseC in house:
#         if abs(houseR - r) + abs(houseC - c) <= size - 1:
#             cnt += 1
#     if 0 <= cnt * m - (size * size + (size - 1) * (size - 1)):
#         return cnt
#     return 0
#
# t = int(input())
# for tc in range(1, t + 1):
#     n, m = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     house = []
#     for r in range(n):
#         for c in range(n):
#             if arr[r][c] == 1:
#                 house.append((r, c))
#
#     maxRes = -math.inf
#     for r in range(n):
#         for c in range(n):
#             for i in range(1, n + 2):
#                 maxRes = max(maxRes, simul(r, c, i))
#     print(f'#{tc} {maxRes}')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    price = [k * k + (k - 1) * (k - 1) for k in range(2 * n)]

    home = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                home.append([i, j])

    Max = -21e8
    for i in range(n):
        for j in range(n):
            home_cnt = [0] * (2 * n)
            for k in home:
                dist = abs(k[0] - i) + abs(k[1] - j) + 1
                home_cnt[dist] += 1

            for l in range(1, n + 2):
                home_cnt[l] += home_cnt[l - 1]
                if price[l] <= home_cnt[l] * m:
                    if Max < home_cnt[l]:
                        Max = home_cnt[l]

    print(f'#{tc} {Max}')