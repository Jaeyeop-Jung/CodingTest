# import heapq
# import math
#
# dR = [0, 1, 0, -1]
# dC = [1, 0, -1, 0]
#
# def solution(M, S, D):
#     n = len(M)
#     m = len(M[0])
#     dp = [[math.inf] * m for _ in range(n)]
#     startC, startR = S
#     dp[startR][startC] = 0
#
#     h = [[0, startR, startC]]
#     while h:
#         cost, curR, curC, = heapq.heappop(h)
#         if dp[curR][curC] < cost:
#             continue
#         for i in range(4):
#             movedR, movedC = curR + dR[i], curC + dC[i]
#             if not 0 <= movedR < n or not 0 <= movedC < m:
#                 continue
#             if M[movedR][movedC] == 1:
#                 continue
#             totalCost = cost + 1
#             if totalCost < dp[movedR][movedC]:
#                 heapq.heappush(h, [totalCost, movedR, movedC])
#                 dp[movedR][movedC] = totalCost
#
#     destinationC, destinationR = D
#     return dp[destinationR][destinationC] if dp[destinationR][destinationC] != math.inf else -1

# import math
#
# dR = [0, 1, 0, -1]
# dC = [1, 0, -1, 0]
#
# def dfs(board, visited, r, c, tR, tC, cost):
#     if r == tR and c == tC:
#         global result
#         global resultCost
#         if cost == resultCost:
#             result += 1
#         elif cost < resultCost:
#             result = 1
#             resultCost = cost
#         return
#     for i in range(4):
#         movedR, movedC = r + dR[i], c + dC[i]
#         if not 0 <= movedR < len(board) or not 0 <= movedC < len(board[0]):
#             continue
#         if board[movedR][movedC] == 1 or visited[movedR][movedC]:
#             continue
#         visited[movedR][movedC] = True
#         dfs(board, visited, movedR, movedC, tR, tC, cost + 1)
#         visited[movedR][movedC] = False
#
#
# result = 0
# resultCost = math.inf
# def solution(M, S, D):
#     visited = [[False] * len(M[0]) for _ in range(len(M))]
#     startC, startR = S
#     tC, tR = D
#     visited[startR][startC] = True
#     dfs(M, visited, startR, startC, tR, tC, 0)
#     return result

import heapq
import math

dR = [1, -1, 0, 0]
dC = [0, 0, -1, 1]


def solution(M, S, D):
    n = len(M)
    m = len(M[0])
    dp = [[math.inf] * m for _ in range(n)]
    startC, startR = S
    destC, destR = D
    dp[startR][startC] = 0

    h = [[0, startR, startC, [0, 0, 0, 0]]]
    path = [0, 0, 0, 0]
    while h:
        cost, curR, curC, route = heapq.heappop(h)
        if curR == destR and curC == destC:
            if cost <= dp[curR][curC]:
                path = route
        if dp[curR][curC] < cost:
            continue
        for i in range(4):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < m:
                continue
            if M[movedR][movedC] == 1:
                continue
            totalCost = cost + 1
            if totalCost <= dp[movedR][movedC]:
                tempRoute = route[:]
                tempRoute[i] += 1
                heapq.heappush(h, [totalCost, movedR, movedC, tempRoute])
                dp[movedR][movedC] = totalCost

    return str(path[0]) + '/' + str(path[1]) + '/' + str(path[2]) + '/' + str(path[3])

print(solution([[0,0,0],[0,1,0],[0,0,0]], [0,0],[2,2]))
# print(solution([
#     [0, 0, 1, 0, 0, 0, 0, 0],
#     [0, 0, 0, 1, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0, 1, 0, 0],
#     [0, 1, 1, 0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1]], [0, 0], [6, 3]))