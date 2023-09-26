import math
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = []
virus = []
target = 0
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(n):
        if temp[c] == 2:
            virus.append((r, c))
        elif temp[c] == 0:
            target += 1
    arr.append(temp)

def bfs(case):
    visited = [[math.inf] * n for _ in range(n)]
    q = deque()
    case = [(virus[i][0], virus[i][1]) for i in case]
    tempRes = 0
    cnt = 0
    for r, c in case:
        visited[r][c] = 0
        q.append((r, c, 0))
    while q:
        r, c, cost = q.popleft()
        for i in range(4):
            movedR, movedC = r + dR[i], c + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if visited[movedR][movedC] != math.inf or arr[movedR][movedC] == 1:
                continue
            if arr[movedR][movedC] == 0:
                q.append((movedR, movedC, cost + 1))
                visited[movedR][movedC] = cost + 1
                tempRes = max(tempRes, cost + 1)
                cnt += 1
            else:
                q.append((movedR, movedC, cost + 1))
                visited[movedR][movedC] = cost + 1

    if cnt == target:
        return tempRes
    else:
        return math.inf


res = math.inf
for i in combinations([i for i in range(len(virus))], m):
    res = min(res, bfs(i))

print(res if res != math.inf else -1)