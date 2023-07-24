import sys
from collections import deque

input = sys.stdin.readline

dR = [1, 2, 2, 1, -1, -2, -2, -1]
dC = [2, 1, -1, -2, -2, -1, 1, 2]

t = int(input())
for _ in range(t):
    n = int(input())
    sR, sC = map(int, input().split())
    eR, eC, = map(int, input().split())

    arr = [[sys.maxsize] * n for _ in range(n)]
    q = deque()
    q.append([sR, sC, 0])
    arr[sR][sC] = 0
    flag = True
    if sR == eR and sC == eC:
        print(0)
    else:
        while q and flag:
            r, c, cost, = q.popleft()
            for i in range(len(dR)):
                movedR, movedC = r + dR[i], c + dC[i]
                if not 0 <= movedR < n or not 0 <= movedC < n:
                    continue
                if arr[movedR][movedC] != sys.maxsize:
                    continue
                arr[movedR][movedC] = cost + 1
                if movedR == eR and movedC == eC:
                    flag = False
                    print(cost + 1)
                    break
                q.append([movedR, movedC, cost + 1])

    # print(arr[eR][eC])