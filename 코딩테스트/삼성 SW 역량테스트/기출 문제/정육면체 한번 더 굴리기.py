from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def diceMove(dice, d):
    if d == 0:
        newDice = [7 - dice[1], dice[0], dice[2]]
    elif d == 1:
        newDice = [7 - dice[2], dice[1], dice[0]]
    elif d == 2:
        newDice = [dice[1], 7 - dice[0], dice[2]]
    else:
        newDice = [dice[2], dice[1], 7 - dice[0]]
    return newDice

def notInRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return True
    return False

def getScore(r, c):
    q = deque()
    q.append([r, c])
    cnt = 1
    visited = [[False] * n for _ in range(n)]
    visited[r][c] = True
    while q:
        curR, curC, = q.popleft()
        for i in range(4):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if notInRange(movedR, movedC) or arr[movedR][movedC] != arr[r][c] or visited[movedR][movedC]:
                continue
            cnt += 1
            visited[movedR][movedC] = True
            q.append([movedR, movedC])
    return arr[r][c] * cnt


n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dice = [1, 3, 2]
d = 0
dice = diceMove(dice, 0)
r, c = 0, 1
result = getScore(r, c)
for _ in range(m - 1):
    if arr[r][c] < 7 - dice[0]:
        d = (d + 1) % 4
    elif 7 - dice[0] < arr[r][c]:
        d = (d - 1) % 4
    movedR, movedC = r + dR[d], c + dC[d]
    if notInRange(movedR, movedC):
        d = (d + 2) % 4
        movedR, movedC = r + dR[d], c + dC[d]
    dice = diceMove(dice, d)
    result += getScore(movedR, movedC)
    r, c = movedR, movedC

print(result)
