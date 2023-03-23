
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def bomb(c):
    r = 0
    for curR in range(n):
        if arr[curR][c] != 0:
            r = curR
            break

    for d in range(4):
        curR, curC = r, c
        for _ in range(arr[r][c] - 1):
            movedR, movedC = curR + dR[d], curC + dC[d]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                break
            arr[movedR][movedC] = 0
            curR, curC = movedR, movedC
    arr[r][c] = 0


def down():
    for c in range(n):
        temp = []
        for r in range(n - 1, -1, -1):
            if arr[r][c] != 0:
                temp.append(arr[r][c])
        idx = 0
        for r in range(n - 1, n - 1 - len(temp), -1):
            arr[r][c] = temp[idx]
            idx += 1
        for r in range(n - len(temp) - 1, -1, -1):
            arr[r][c] = 0

for _ in range(m):
    c = int(input())
    bomb(c - 1)
    down()

for i in arr:
    print(*i)
