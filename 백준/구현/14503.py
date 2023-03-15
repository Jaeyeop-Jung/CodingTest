import sys

input = sys.stdin.readline

dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
clean = [[False] * m for _ in range(n)]

def isInRange(r, c):
    if not 0 <= r < n or not 0 <= c < m:
        return False
    return True

while True:
    if not clean[r][c]:
        clean[r][c] = True
    for i in range(4):
        nextD = (d - i - 1) % 4
        movedR, movedC, = r + dR[nextD], c + dC[nextD]
        if isInRange(movedR, movedC) and arr[movedR][movedC] == 0 and not clean[movedR][movedC]:
            d = nextD
            r, c = movedR, movedC
            break
    else:
        back = (d + 2) % 4
        movedR, movedC, = r + dR[back], c + dC[back]
        if arr[movedR][movedC] == 1 or not isInRange(movedR, movedC):
            break
        r, c = movedR, movedC

result = 0
for r in range(n):
    for c in range(m):
        if clean[r][c]:
            result += 1
print(result)