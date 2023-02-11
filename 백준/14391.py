# TODO 틀림

dR = [0, 1]
dC = [1, 0]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

def check():
    for i in visited:
        for j in i:
            if not j:
                return False
    return True

def dfs(visited, curR, curC, route, d):
    if check():
        global result
        result = max(result, sum(map(int, route)))
        return

    if d == -1:
        for i in range(2):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < m:
                continue
            if visited[movedR][movedC]:
                continue
            visited[movedR][movedC] = True
            route[-1] += arr[movedR][movedC]
            dfs(visited, movedR, movedC, route, i)
            visited[movedR][movedC] = False
            route[-1] = route[-1][:-1]
    else:
        movedR, movedC = curR + dR[d], curC + dC[d]
        if (0 <= movedR < n and 0 <= movedC < m) and not visited[movedR][movedC]:
            visited[movedR][movedC] = True
            route[-1] += arr[movedR][movedC]
            dfs(visited, movedR, movedC, route, d)
            visited[movedR][movedC] = False
            route[-1] = route[-1][:-1]

    for r in range(n):
        for c in range(m):
            if not visited[r][c]:
                visited[r][c] = True
                dfs(visited, r, c, route + [arr[r][c]], -1)
                visited[r][c] = False



result = 0
visited[0][0] = True
dfs(visited, 0, 0, [arr[0][0]], -1)
print(result)