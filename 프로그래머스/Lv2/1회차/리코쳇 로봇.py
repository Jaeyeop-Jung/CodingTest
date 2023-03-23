import math
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def solution(board):
    n = len(board)
    m = len(board[0])
    dp = [[math.inf] * m for _ in range(n)]
    curR, curC = -1, -1
    tR, tC = -1, -1
    for r in range(n):
        for c in range(m):
            if board[r][c] == 'R':
                curR, curC = r, c
            if board[r][c] == 'G':
                tR, tC = r, c

    q = deque()
    q.append([curR, curC, 0])
    dp[curR][curC] = 0
    while q:
        startR, startC, cost, = q.popleft()
        for i in range(4):
            curR, curC = startR, startC
            while True:
                movedR, movedC = curR + dR[i], curC + dC[i]
                if not 0 <= movedR < n or not 0 <= movedC < m:
                    break
                if board[movedR][movedC] == 'D':
                    break
                curR, curC = movedR, movedC
            if cost + 1 < dp[curR][curC]:
                q.append([curR, curC, cost + 1])
                dp[curR][curC] = cost + 1

    return dp[tR][tC] if dp[tR][tC] != math.inf else -1


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))
