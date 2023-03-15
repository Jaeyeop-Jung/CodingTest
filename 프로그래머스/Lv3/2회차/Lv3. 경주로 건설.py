import math
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m = 0, 0

def isInRange(r, c):
    if not 0 <= r < n or not 0 <= c < m:
        return False
    return True

def solution(board):
    global n, m
    n = len(board)
    m = len(board[0])


    q = deque()
    visited = [[[math.inf] * 4 for _ in range(m)] for _ in range(n)]
    for i in range(4):
        visited[0][0][i] = 0
    if board[0][1] == 0:
        visited[0][1][0] = 100
        q.append([0, 1, 0, 100])
    if board[1][0] == 0:
        visited[1][0][1] = 100
        q.append([1, 0, 1, 100])
    while q:
        curR, curC, d, cost, = q.popleft()
        for i in range(len(dR)):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if not isInRange(movedR, movedC) or board[movedR][movedC] == 1:
                continue
            nextCost = cost + 100
            if i != d:
                nextCost += 500
            if visited[movedR][movedC][i] <= nextCost:
                continue
            q.append([movedR, movedC, i, nextCost])
            visited[movedR][movedC][i] = nextCost
    return min(visited[-1][-1])

print(solution(
    [
        [0, 0, 0],
        [1, 0, 1],
        [0, 0, 0]
    ]
))