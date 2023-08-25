
dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def dfs(processor, idx, cnt, cable):
    if idx == len(processor):
        global res, resCable
        if res == cnt:
            resCable = min(resCable, cable)
        elif res < cnt:
            resCable = cable
            res = cnt
        return

    r, c = processor[idx]
    for d in range(len(dR)):
        curR, curC = r, c
        visited = []
        while True:
            movedR, movedC = curR + dR[d], curC + dC[d]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                for i in range(len(visited)):
                    visitR, visitC, = visited[i]
                    arr[visitR][visitC] = 1
                dfs(processor, idx + 1, cnt + 1, cable + len(visited))
                for i in range(len(visited)):
                    visitR, visitC, = visited[i]
                    arr[visitR][visitC] = 0
                break
            if arr[movedR][movedC] != 0:
                break
            visited.append((movedR, movedC))
            curR, curC = movedR, movedC
    dfs(processor, idx + 1, cnt, cable)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    processor = []
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 1:
                if r == 0 or r == n - 1 or c == 0 or c == n - 1:
                    cnt += 1
                else:
                    processor.append((r, c))
    res = cnt
    resCable = 0
    dfs(processor, 0, cnt, 0)
    print(f'#{tc} {resCable}')