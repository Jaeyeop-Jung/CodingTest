
n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def rotate(arr, r1, c1, r2, c2):
    curR, curC = r1, c1
    temp = arr[r1][c1]
    movement = [c2 - c1, r2 - r1] * 2
    for i in range(4):
        for _ in range(movement[i]):
            movedR, movedC = curR + dR[i], curC + dC[i]
            temp2 = arr[movedR][movedC]
            arr[movedR][movedC] = temp
            temp = temp2
            curR, curC = movedR, movedC

def average(arr, r1, c1, r2, c2):
    newArr = [i[:] for i in arr]
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            sumTemp = arr[r][c]
            cnt = 1
            for d in range(4):
                nextR = r + dR[d]
                nextC = c + dC[d]
                if not 0 <= nextR < n or not 0 <= nextC < m:
                    continue
                cnt += 1
                sumTemp += arr[nextR][nextC]
            newArr[r][c] = sumTemp // cnt
    return newArr

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    rotate(arr, r1 - 1, c1 - 1, r2 - 1, c2 - 1)
    arr = average(arr, r1 - 1, c1 - 1, r2 - 1, c2 - 1)

for i in arr:
    print(*i)