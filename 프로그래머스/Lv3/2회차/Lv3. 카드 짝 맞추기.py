import math
from collections import defaultdict
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def inRange(r, c):
    if 0 <= r < 4 and 0 <= c < 4:
        return True
    return False

def bfs(board, r, c, tR, tC):
    q = deque()
    q.append([r, c, 0])
    visited = [[math.inf] * 4 for _ in range(4)]
    visited[r][c] = 0
    while q:
        curR, curC, cost, = q.popleft()
        for i in range(4):
            # 1회 이동
            movedR, movedC = curR + dR[i], curC + dC[i]
            if inRange(movedR, movedC) and cost + 1 < visited[movedR][movedC]:
                visited[movedR][movedC] = cost + 1
                q.append([movedR, movedC, cost + 1])
                if movedR == tR and movedC == tC:
                    return cost + 1

            # ctrl 이동
            movedR, movedC = curR + dR[i], curC + dC[i]
            while inRange(movedR, movedC) and board[movedR][movedC] == 0:
                movedR, movedC = movedR + dR[i], movedC + dC[i]
            if inRange(movedR, movedC) and cost + 1 < visited[movedR][movedC]:
                visited[movedR][movedC] = cost + 1
                q.append([movedR, movedC, cost + 1])
                if movedR == tR and movedC == tC:
                    return cost + 1
            elif not inRange(movedR, movedC) and cost + 1 < visited[movedR - dR[i]][movedC - dC[i]]:
                visited[movedR - dR[i]][movedC - dC[i]] = cost + 1
                q.append([movedR - dR[i], movedC - dC[i], cost + 1])
                if movedR - dR[i] == tR and movedC - dC[i] == tC:
                    return cost + 1
    return visited[tR][tC]

def dfs(board, cards, visited, r, c, cost):
    global res
    if res < cost:
        return
    if all(visited):
        res = min(res, cost)
        return

    for i in range(1, len(cards) + 1):
        if not visited[i - 1]:
            visited[i - 1] = True
            r1, c1 = cards[i][0]
            r2, c2 = cards[i][1]

            # 1번 선택
            distTo1 = bfs(board, r, c, r1, c1)
            board[r1][c1] = 0
            distTo2 = bfs(board, r1, c1, r2, c2)
            board[r2][c2] = 0
            dfs(board, cards, visited, r2, c2, cost + distTo1 + distTo2 + 2)
            board[r1][c1] = i
            board[r2][c2] = i

            # 2번 선택
            distTo2 = bfs(board, r, c, r2, c2)
            board[r2][c2] = 0
            distTo1 = bfs(board, r2, c2, r1, c1)
            board[r1][c1] = 0
            dfs(board, cards, visited, r1, c1, cost + distTo1 + distTo2 + 2)
            board[r1][c1] = i
            board[r2][c2] = i

            visited[i - 1] = False

res = math.inf
def solution(board, curR, curC):
    cards = defaultdict(list)
    for r in range(4):
        for c in range(4):
            if board[r][c] != 0:
                cards[board[r][c]].append([r, c])
    dfs(board, cards, [False] * len(cards), curR, curC, 0)
    return res


print(solution(
    [[1, 2, 3, 4],
     [5, 6, 0, 0],
     [0, 0, 6, 5],
     [4, 3, 2, 1]],
    0, 0))
# print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))
# print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1))