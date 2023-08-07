import math
from itertools import permutations
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def bfs(r, c):
    visited = [[math.inf] * m for _ in range(n)]
    visited[r][c] = 0
    q = deque()
    q.append((r, c, 0))
    while q:
        r, c, cost, = q.popleft()
        for i in range(4):
            movedR, movedC = r + dR[i], c + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < m:
                continue
            if visited[movedR][movedC] != math.inf or arr[movedR][movedC] == 'x':
                continue
            q.append((movedR, movedC, cost + 1))
            visited[movedR][movedC] = cost + 1
    return visited

while True:
    m, n = map(int, input().split())
    if n == 0 and m == 0:
        break

    arr = []
    target = []
    for r in range(n):
        temp = list(input())
        for c in range(m):
            if temp[c] == 'o':
                sR, sC = r, c
            elif temp[c] == '*':
                target.append((r, c))
        arr.append(temp)

    target = [[sR, sC]] + target
    distance = [[0] * (len(target)) for _ in range(len(target))]
    for start in range(len(target)):
        startR, startC = target[start]
        tempDistance = bfs(startR, startC)
        for end in range(start + 1, len(target)):
            endR, endC = target[end]
            distance[start][end] = tempDistance[endR][endC]
            distance[end][start] = tempDistance[endR][endC]


    res = math.inf
    for i in permutations([i for i in range(1, len(target))], len(target) - 1):
        cur = 0
        temp = 0
        for next in i:
            temp += distance[cur][next]
            if temp == math.inf:
                break
            cur = next
        res = min(res, temp)

    print(res if res != math.inf else -1)


