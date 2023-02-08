
dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

r, c, k, = map(int, input().split())
arr = [list(input()) for _ in range(r)]

def dfs(visited, curR, curC, cnt):
    if 0 == curR and c - 1 == curC:
        if cnt == k:
            global result
            result += 1
        return

    for i in range(4):
        movedR, movedC = curR + dR[i], curC + dC[i]
        if not 0 <= movedR < r or not 0 <= movedC < c:
            continue
        if visited[movedR][movedC] or arr[movedR][movedC] == 'T':
            continue
        if k < cnt:
            continue
        visited[movedR][movedC] = True
        dfs(visited, movedR, movedC, cnt + 1)
        visited[movedR][movedC] = False

result = 0
visited = [[False] * c for _ in range(r)]
visited[r - 1][0] = True
dfs(visited, r - 1, 0, 1)
print(result)
