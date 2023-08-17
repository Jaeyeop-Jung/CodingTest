import math
from collections import deque

dR = [0, 1, 1, 1, 0, -1, -1, -1]
dC = [1, 1, 0, -1, -1, -1, 0, 1]

def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return False
    return True

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[[math.inf] * 2 for _ in range(n)] for _ in range(n)]
q = deque()
flag = False
for r in range(n):
    for c in range(n):
        if arr[r][c] == 'B' and r + 1 < n and arr[r + 1][c] == 'B' and r + 2 < n and arr[r + 2][c] == 'B':
            sR = r + 1
            sC = c
            visited[sR][sC][0] = 0
            q.append((sR, sC, 0, 0))
        elif arr[r][c] == 'B' and c + 1 < n and arr[r][c + 1] == 'B' and c + 2 < n and arr[r][c + 2] == 'B':
            sR = r
            sC = c + 1
            visited[sR][sC][1] = 0
            q.append((sR, sC, 1, 0))

        if arr[r][c] == 'E' and r + 1 < n and arr[r + 1][c] == 'E' and r + 2 < n and arr[r + 2][c] == 'E':
            eR = r + 1
            eC = c
            eShape = 0
        elif arr[r][c] == 'E' and c + 1 < n and arr[r][c + 1] == 'E' and c + 2 < n and arr[r][c + 2] == 'E':
            eR = r
            eC = c + 1
            eShape = 1

while q:
    r, c, shape, cost = q.popleft()
    if r == eR and c == eC and shape == eShape:
        break

    # -
    if shape == 1:
        # up
        leftCheck = [-1, -2, -3]
        for d in leftCheck:
            movedR, movedC = r + dR[d], c + dC[d]
            if not inRange(movedR, movedC) or arr[movedR][movedC] == '1':
                break
        else:
            if visited[r - 1][c][shape] == math.inf:
                q.append((r - 1, c, shape, cost + 1))
                visited[r - 1][c][shape] = cost + 1

        # down
        rightCheck = [1, 2, 3]
        for d in rightCheck:
            movedR, movedC = r + dR[d], c + dC[d]
            if not inRange(movedR, movedC) or arr[movedR][movedC] == '1':
                break
        else:
            if visited[r + 1][c][shape] == math.inf:
                q.append((r + 1, c, shape, cost + 1))
                visited[r + 1][c][shape] = cost + 1

        # left
        if inRange(r, c - 2) and arr[r][c - 2] != '1' and visited[r][c - 1][shape] == math.inf:
            q.append((r, c - 1, shape, cost + 1))
            visited[r][c - 1][shape] = cost + 1

        # right
        if inRange(r, c + 2) and arr[r][c + 2] != '1' and visited[r][c + 1][shape] == math.inf:
            q.append((r, c + 1, shape, cost + 1))
            visited[r][c + 1][shape] = cost + 1
    # |
    else:
        # left
        leftCheck = [3, 4, 5]
        for d in leftCheck:
            movedR, movedC = r + dR[d], c + dC[d]
            if not inRange(movedR, movedC) or arr[movedR][movedC] == '1':
                break
        else:
            if visited[r][c - 1][shape] == math.inf:
                q.append((r, c - 1, shape, cost + 1))
                visited[r][c - 1][shape] = cost + 1

        # right
        rightCheck = [-1, 0, 1]
        for d in rightCheck:
            movedR, movedC = r + dR[d], c + dC[d]
            if not inRange(movedR, movedC) or arr[movedR][movedC] == '1':
                break
        else:
            if visited[r][c + 1][shape] == math.inf:
                q.append((r, c + 1, shape, cost + 1))
                visited[r][c + 1][shape] = cost + 1

        # up
        if inRange(r - 2, c) and arr[r - 2][c] != '1' and visited[r - 1][c][shape] == math.inf:
            q.append((r - 1, c, shape, cost + 1))
            visited[r - 1][c][shape] = cost + 1

        # down
        if inRange(r + 2, c) and arr[r + 2][c] != '1' and visited[r + 1][c][shape] == math.inf:
            q.append((r + 1, c, shape, cost + 1))
            visited[r + 1][c][shape] = cost + 1

    if visited[r][c][shape ^ 1] == math.inf:
        for d in range(8):
            movedR, movedC = r + dR[d], c + dC[d]
            if not inRange(movedR, movedC) or arr[movedR][movedC] == '1':
                break
        else:
            q.append((r, c, shape ^ 1, cost + 1))
            visited[r][c][shape ^ 1] = cost + 1

print(visited[eR][eC][eShape] if visited[eR][eC][eShape] != math.inf else 0)