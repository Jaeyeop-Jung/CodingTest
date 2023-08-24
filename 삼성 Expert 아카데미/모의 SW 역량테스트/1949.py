
dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def dfs(visited, r, c, broken, cnt):
    global res
    res = max(res, cnt)

    cur = arr[r][c]
    for i in range(len(dR)):
        movedR, movedC = r + dR[i], c + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < n:
            continue
        if visited[movedR][movedC]:
            continue

        if arr[movedR][movedC] < cur:
            visited[movedR][movedC] = True
            dfs(visited, movedR, movedC, broken, cnt + 1)
            visited[movedR][movedC] = False
        else:
            if broken or cur <= arr[movedR][movedC] - k:
                continue
            temp = arr[movedR][movedC]
            arr[movedR][movedC] = cur - 1
            visited[movedR][movedC] = True
            dfs(visited, movedR, movedC, True, cnt + 1)
            arr[movedR][movedC] = temp
            visited[movedR][movedC] = False

t = int(input())
for test_case in range(1, t + 1):
    n, k, = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    start = []
    maxHeight = max(map(max, arr))
    for r in range(n):
        for c in range(n):
            if arr[r][c] == maxHeight:
                start.append([r, c])

    res = 0
    for r, c in start:
        visited = [[False] * n for _ in range(n)]
        visited[r][c] = True
        dfs(visited, r, c, False, 1)

    print(f'#{test_case} {res}')