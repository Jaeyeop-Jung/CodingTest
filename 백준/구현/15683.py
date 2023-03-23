import math

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

sight = [[0], [0, -2], [0, -1], [0, -1, -2], [0, -1, -2, -3]]

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

camera = []
for r in range(n):
    for c in range(m):
        if 1 <= arr[r][c] <= 5:
            camera.append([r, c])

def count(arr):
    empty = 0
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 0:
                empty += 1
    return empty

def capture(arr, r, c, d):
    while True:
        movedR, movedC = r + dR[d], c + dC[d]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            break
        if arr[movedR][movedC] == 6:
            break
        if arr[movedR][movedC] == 0:
            arr[movedR][movedC] = '#'
        r, c = movedR, movedC

result = math.inf
def dfs(arr, cnt):
    if cnt == len(camera):
        global result
        result = min(result, count(arr))
        return

    startR, startC = camera[cnt]
    for d in range(4):
        newArr = [i[:] for i in arr]
        for each in sight[arr[startR][startC] - 1]:
            capture(newArr, startR, startC, d + each)
        dfs(newArr, cnt + 1)


dfs(arr, 0)
print(result)