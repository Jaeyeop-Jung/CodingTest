# TODO 틀림

import sys
input = sys.stdin.readline

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

result = 0
def dfs(visited, pr, pc, r, c, total, cnt):
    if cnt == 4:
        global result
        visited[r][c] = True
        result = max(result, total)
        visited[r][c] = False
        return

    visited[r][c] = True
    for i in range(4):
        movedR = r + dRow[i]
        movedC = c + dColumn[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if visited[movedR][movedC]:
            continue
        dfs(visited, r, c, movedR, movedC, total + board[movedR][movedC], cnt + 1)
        visited[movedR][movedC] = False
    if pr != -1 and pc != -1:
        for i in range(4):
            movedR = pr + dRow[i]
            movedC = pc + dColumn[i]
            if not 0 <= movedR < n or not 0 <= movedC < m:
                continue
            if visited[movedR][movedC]:
                continue
            dfs(visited, pr, pc, movedR, movedC, total + board[movedR][movedC], cnt + 1)
            visited[movedR][movedC] = False

visited = [[False] * m for i in range(n)]
for r in range(n):
    for c in range(m):
        dfs(visited, -1, -1, r, c, board[r][c], 1)

print(result)