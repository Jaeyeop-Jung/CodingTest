from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, q, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2 ** n)]
ls = list(map(int, input().split()))

def rotate(size):
    for r in range(0, 2 ** n, 2 ** size):
        for c in range(0, 2 ** n, 2 ** size):
            rotateRect = deque()
            for curC in range(c, c + 2 ** size):
                for curR in range(r + 2 ** size - 1, r - 1, - 1):
                    rotateRect.append(arr[curR][curC])
            for curR in range(r, r + 2 ** size):
                for curC in range(c, c + 2 ** size):
                    arr[curR][curC] = rotateRect.popleft()

def unfreeze():
    newArr = [i[:] for i in arr]
    for r in range(2 ** n):
        for c in range(2 ** n):
            if arr[r][c] == 0:
                continue
            cnt = 0
            for d in range(4):
                movedR, movedC = r + dR[d], c + dC[d]
                if not 0 <= movedR < 2 ** n or not 0 <= movedC < 2 ** n:
                    continue
                if arr[movedR][movedC] != 0:
                    cnt += 1
            if cnt < 3:
                newArr[r][c] -= 1
    return newArr

for l in ls:
    rotate(l)
    arr = unfreeze()

size = 0
visited = [[False] * 2 ** n for _ in range(2 ** n)]
for r in range(2 ** n):
    for c in range(2 ** n):
        if not visited[r][c] and arr[r][c] != 0:
            q = deque()
            q.append([r, c])
            visited[r][c] = True
            cnt = 1
            while q:
                curR, curC, = q.popleft()
                for d in range(4):
                    movedR, movedC = curR + dR[d], curC + dC[d]
                    if not 0 <= movedR < 2 ** n or not 0 <= movedC < 2 ** n:
                        continue
                    if arr[movedR][movedC] == 0 or visited[movedR][movedC]:
                        continue
                    q.append([movedR, movedC])
                    cnt += 1
                    visited[movedR][movedC] = True
            size = max(size, cnt)

print(sum(map(sum, arr)))
print(size)