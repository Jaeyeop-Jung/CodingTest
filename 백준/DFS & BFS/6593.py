import math
import sys
from collections import deque

input = sys.stdin.readline

dL = [1, -1, 0, 0, 0, 0]
dR = [0, 0, 0, 1, 0, -1]
dC = [0, 0, 1, 0, -1, 0]

while True:
    l, r, c, = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    arr = []
    for l1 in range(l):
        temp = []
        for r1 in range(r):
            temp2 = list(input().strip())
            for c1 in range(c):
                if temp2[c1] == 'S':
                    sL, sR, sC = l1, r1, c1
                elif temp2[c1] == 'E':
                    eL, eR, eC = l1, r1, c1
            temp.append(temp2)
        arr.append(temp)

        input()

    visited = [[[math.inf] * c for _ in range(r)] for _ in range(l)]
    visited[sL][sR][sC] = 0
    q = deque([[sL, sR, sC, 0]])
    while q:
        curL, curR, curC, cost = q.popleft()
        for i in range(6):
            movedL, movedR, movedC = curL + dL[i], curR + dR[i], curC + dC[i]
            if not 0 <= movedL < l or not 0 <= movedR < r or not 0 <= movedC < c:
                continue
            if arr[movedL][movedR][movedC] == '#' or visited[movedL][movedR][movedC] != math.inf:
                continue
            visited[movedL][movedR][movedC] = cost + 1
            q.append([movedL, movedR, movedC, cost + 1])

    print(f'Escaped in {visited[eL][eR][eC]} minute(s).' if visited[eL][eR][eC] != math.inf else 'Trapped!')