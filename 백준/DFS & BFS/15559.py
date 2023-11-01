import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

res = 0
def dfs(arr, visited, r, c, s):
    cur = arr[r][c]
    if cur == 'E':
        movedR, movedC = r + 0, c + 1
    elif cur == 'S':
        movedR, movedC = r + 1, c + 0
    elif cur == 'W':
        movedR, movedC = r + 0, c - 1
    else:
        movedR, movedC = r - 1, c + 0

    if not 0 <= movedR < n or not 0 <= movedC < m:
        return
    if visited[movedR][movedC]:
        global res
        res -= 1
        return
    if (movedR, movedC) in s:
        return
    s.add((movedR, movedC))
    dfs(arr, visited, movedR, movedC, s)



visited = [[False] * m for _ in range(n)]
for r in range(n):
    for c in range(m):
        if not visited[r][c]:
            s = set()
            s.add((r, c))
            dfs(arr, visited, r, c, s)
            for r1, c1 in s:
                visited[r1][c1] = True
            res += 1

print(res)