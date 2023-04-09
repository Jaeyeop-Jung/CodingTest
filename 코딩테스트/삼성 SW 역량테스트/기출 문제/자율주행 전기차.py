'''
1. 가장 가까운 승객을 찾는다. 만약 그게 여러개라면 가장 작은 행, 가장 작은 열을 기준으로
2. 승객을 태우고, 목적지까지 이동한다.
3. 목적지에 도달할 수 있으면 승객을 태우고 난 뒤에 소모한 배터리 2배만큼 흭득한다.

* 마지막 순간에도 배터리는 충전된다
* 목적지에 도달할 때 배터리가 0이 되도 2배로 충전되서 살아난다
'''
import math
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, battery, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r - 1, c - 1
passenger = {}
for num in range(m):
    sR, sC, eR, eC = map(int, input().split())
    passenger[num] = [sR - 1, sC - 1, eR - 1, eC - 1]

def getDistance(r, c):
    visited = [[math.inf] * n for _ in range(n)]
    visited[r][c] = 0
    q = deque()
    q.append([r, c, 0])
    while q:
        curR, curC, cost, = q.popleft()
        for i in range(4):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if visited[movedR][movedC] != math.inf or arr[movedR][movedC] == 1:
                continue
            q.append([movedR, movedC, cost + 1])
            visited[movedR][movedC] = cost + 1
    return visited

def goPassenger():
    global battery, r, c
    distance = getDistance(r, c)
    tR, tC = n, n
    dist = math.inf
    tNum = m
    for passengerNum in passenger:
        pR, pC, _, _, = passenger[passengerNum]
        if distance[pR][pC] < dist:
            tR, tC = pR, pC
            dist = distance[pR][pC]
            tNum = passengerNum
        elif distance[pR][pC] == dist and pR < tR:
            tR, tC = pR, pC
            dist = distance[pR][pC]
            tNum = passengerNum
        elif distance[pR][pC] == dist and pR == tR and pC < tC:
            tR, tC = pR, pC
            dist = distance[pR][pC]
            tNum = passengerNum

    battery -= dist
    r, c = tR, tC
    return tNum

def goDestination(passengerNum):
    global battery, r, c
    distance = getDistance(r, c)
    _, _, tR, tC = passenger[passengerNum]
    dist = distance[tR][tC]

    battery -= dist
    r, c = tR, tC
    if battery < 0:
        return
    battery += dist * 2
    del passenger[passengerNum]

for _ in range(m):
    curPassengerNum = goPassenger()
    if battery < 0:
        print(-1)
        break
    goDestination(curPassengerNum)
    if battery < 0:
        print(-1)
        break
else:
    print(battery)

