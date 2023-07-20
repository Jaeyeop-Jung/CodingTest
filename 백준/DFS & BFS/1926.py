import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(arr, visited, r, c, cnt):
    global temp
    temp += 1
    for i in range(4):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if visited[movedR][movedC] or arr[movedR][movedC] == 0:
            continue
        visited[movedR][movedC] = True
        dfs(arr, visited, movedR, movedC, cnt + 1)

resCnt = 0
res = 0
visited = [[False] * m for _ in range(n)]
for r in range(n):
    for c in range(m):
        if not visited[r][c] and arr[r][c] == 1:
            temp = 0
            visited[r][c] = True
            dfs(arr, visited, r, c, 1)
            resCnt += 1
            res = max(res, temp)

print(resCnt)
print(res)