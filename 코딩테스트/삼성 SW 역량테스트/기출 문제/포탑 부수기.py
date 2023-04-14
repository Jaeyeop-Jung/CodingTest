import math
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

aR = [0, 1, 1, 1, 0, -1, -1, -1]
aC = [1, 1, 0, -1, -1, -1, 0, 1]

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
mindArr = [[-1] * m for _ in range(n)]

def powerUp(round):
    tR, tC, power, recent = -1, -1, math.inf, -2
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 0:
                continue
            if arr[r][c] < power:
                tR, tC, power, recent = r, c, arr[r][c], mindArr[r][c]
            elif arr[r][c] == power and recent < mindArr[r][c]:
                tR, tC, power, recent = r, c, arr[r][c], mindArr[r][c]
            elif arr[r][c] == power and recent == mindArr[r][c] and tR + tC < r + c:
                tR, tC, power, recent = r, c, arr[r][c], mindArr[r][c]
            elif arr[r][c] == power and recent == mindArr[r][c] and tR + tC == r + c and tC < c:
                tR, tC, power, recent = r, c, arr[r][c], mindArr[r][c]
    arr[tR][tC] += n + m
    mindArr[tR][tC] = round
    return tR, tC

def bfs(sR, sC, tR, tC):
    q = deque()
    q.append([sR, sC, 0, []])
    dp = [[math.inf] * m for _ in range(n)]
    dp[sR][sC] = 0
    path = [[[] for _ in range(m)] for _ in range(n)]
    while q:
        curR, curC, cost, route = q.popleft()
        for i in range(4):
            movedR, movedC = curR + dR[i], curC + dC[i]
            movedR, movedC = movedR % n, movedC % m
            if arr[movedR][movedC] == 0 or dp[movedR][movedC] != math.inf:
                continue
            path[movedR][movedC] = route + [i]
            q.append([movedR, movedC, cost + 1, route + [i]])
            dp[movedR][movedC] = cost + 1
    return dp[tR][tC], path[tR][tC]

def whileAttack(sR, sC, tR, tC, path):
    attackCoord =[]
    attackCoord.append((sR, sC))
    p = arr[sR][sC]
    curR, curC = sR, sC
    for i in path:
        movedR, movedC = (curR + dR[i]) % n, (curC + dC[i]) % m
        if movedR == tR and movedC == tC:
            arr[movedR][movedC] -= p
            if arr[movedR][movedC] <= 0:
                arr[movedR][movedC] = 0
        elif arr[movedR][movedC] - int(p / 2) <= 0:
            arr[movedR][movedC] = 0
        else:
            arr[movedR][movedC] -= int(p / 2)
        attackCoord.append((movedR, movedC))
        curR, curC = movedR, movedC
    return attackCoord

def blackAttack(sR, sC, tR, tC):
    attackCoord = []
    attackCoord.append((sR, sC))
    attackCoord.append((tR, tC))
    p = arr[sR][sC]
    arr[tR][tC] -= p
    if arr[tR][tC] <= 0:
        arr[tR][tC] = 0
    for i in range(8):
        movedR, movedC = (tR + aR[i]) % n, (tC + aC[i]) % m
        if arr[movedR][movedC] == 0 or (movedR == sR and movedC == sC):
            continue
        if arr[movedR][movedC] - int(p / 2) <= 0:
            arr[movedR][movedC] = 0
        else:
            arr[movedR][movedC] -= int(p / 2)
        attackCoord.append((movedR, movedC))
    return attackCoord


def attack(sR, sC):
    tR, tC, power, recent = math.inf, math.inf, -1, -2
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 0 or (sR == r and sC == c):
                continue
            if arr[r][c] > power:
                tR, tC, power, recent = r, c, arr[r][c], mindArr[r][c]
            elif arr[r][c] == power and recent > mindArr[r][c]:
                tR, tC, power, recent = r, c, arr[r][c], mindArr[r][c]
            elif arr[r][c] == power and recent == mindArr[r][c] and tR + tC > r + c:
                tR, tC, power, recent = r, c, arr[r][c], mindArr[r][c]
            elif arr[r][c] == power and recent == mindArr[r][c] and tR + tC == r + c and tC > c:
                tR, tC, power, recent = r, c, arr[r][c], mindArr[r][c]

    cost, path, = bfs(sR, sC, tR, tC)
    if cost == math.inf:
        attackCoord = blackAttack(sR, sC, tR, tC)
    else:
        attackCoord = whileAttack(sR, sC, tR, tC, path)
    return attackCoord

def powerHelp(attackCoord):
    for r in range(n):
        for c in range(m):
            if arr[r][c] != 0 and (r, c) not in attackCoord:
                arr[r][c] += 1

def isFinish():
    cnt = 0
    for r in range(n):
        for c in range(m):
            if 0 < arr[r][c]:
                cnt += 1
    return cnt == 1

for round in range(k):
    # if round == 52:
    #     print()
    if isFinish():
        break
    sR, sC, = powerUp(round)
    if isFinish():
        break
    attackCoord = attack(sR, sC)
    if isFinish():
        break
    powerHelp(attackCoord)
    if isFinish():
        break

print(max(map(max, arr)))