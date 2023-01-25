import sys

input = sys.stdin.readline

WHITE = 0
RED = 1
BLUE = 2

dR = [0, 0, 0, -1, 1]
dC = [0, 1, -1, 0, 0]

n, k, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
pawn = []
for i in range(k):
    r, c, d = map(int, input().split())
    pawn.append([r - 1, c - 1, d])
status = [[[] for _ in range(n)] for _ in range(n)]
for i in range(len(pawn)):
    status[pawn[i][0]][pawn[i][1]].append(i)

def isBlue(movedR, movedC):
    if not 0 <= movedR < n or not 0 <= movedC < n:
        return True
    elif arr[movedR][movedC] == BLUE:
        return True
    return False

def getReverseDirection(d):
    if d % 2 == 0:
        return d - 1
    else:
        return d + 1

def isFinish():
    for r in range(n):
        for c in range(n):
            if 4 <= len(status[r][c]):
                return True
    return False

def moveCoord(height, movedR, movedC):
    for i in status[r][c][height:]:
        d = pawn[i][2]
        pawn[i] = [movedR, movedC, d]


for i in range(1, 1001):
    for j in range(k):
        r, c, d, = pawn[j]
        movedR, movedC = r + dR[d], c + dC[d]
        if isBlue(movedR, movedC):
            d = getReverseDirection(d)
            pawn[j] = [r, c, d]

            movedR, movedC = r + dR[d], c + dC[d]
            if isBlue(movedR, movedC):
                continue
            elif arr[movedR][movedC] == WHITE:
                height = status[r][c].index(j)
                moveCoord(height, movedR, movedC)
                status[movedR][movedC] += status[r][c][height:]
            else:
                height = status[r][c].index(j)
                moveCoord(height, movedR, movedC)
                status[movedR][movedC] += list(reversed(status[r][c][height:]))
        elif arr[movedR][movedC] == WHITE:
            height = status[r][c].index(j)
            moveCoord(height, movedR, movedC)
            status[movedR][movedC] += status[r][c][height:]
        else:
            height = status[r][c].index(j)
            moveCoord(height, movedR, movedC)
            status[movedR][movedC] += list(reversed(status[r][c][height:]))
        status[r][c] = status[r][c][:height]

        if isFinish():
            print(i)
            exit()

print(-1)
