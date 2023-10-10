# 1분 동안 다음 3가지
# 1. 사람들이 가고 싶은 편의점을 향해 최단거리 방향으로 1칸 움직임.
#   여러개라면 [위, 왼, 오, 아래] 순위로 움직임
# 2. 편의점에 도착하면 이 편의점은 지나갈 수 없는 칸이 된다.
# 3. 시간 <= 사람 t번 사람이 가고 싶은 편의점과 가까운 베이스캠프에 간다
#   여기서 행이 작고, 열이 작은 순서
#   이 때 부터 다른 사람은 베이스 캠프에 지나갈 수 없음
import math
from collections import deque

dR = [-1, 0, 0, 1]
dC = [0, -1, 1, 0]

n, m = map(int, input().split())
arr = []
baseCamp = []
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(n):
        if temp[c] == 1:
            baseCamp.append([r, c])
    arr.append(temp)
pyeon = []
for _ in range(m):
    r, c = map(int, input().split())
    pyeon.append([r - 1, c - 1])

def bfs(sR, sC):
    q = deque()
    q.append([sR, sC, 0, []])
    dp = [[math.inf] * n for _ in range(n)]
    dp[sR][sC] = 0
    paths = [[[] for _ in range(n)] for _ in range(n)]
    while q:
        curR, curC, cost, path = q.popleft()
        for i in range(4):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if arr[movedR][movedC] == -1 or dp[movedR][movedC] != math.inf:
                continue
            dp[movedR][movedC] = cost + 1
            paths[movedR][movedC] = path + [i]
            q.append([movedR, movedC, cost + 1, path + [i]])
    return dp, paths

people = []
t = 0
while True:
    # 1번
    for i, v in enumerate(people):
        num, pR, pC, curR, curC = v
        _, paths = bfs(curR, curC)
        d = paths[pR][pC][0]
        people[i] = [num, pR, pC, curR + dR[d], curC + dC[d]]

    # 2번
    for i in range(len(people) - 1, -1, -1):
        num, pR, pC, curR, curC, = people[i]
        if pR == curR and pC == curC:
            people.pop(i)
            arr[pR][pC] = -1
    # 3번
    if t < m:
        pR, pC = pyeon.pop(0)
        people.append([t, pR, pC])
        dp, paths = bfs(pR, pC)
        temp = [[bR, bC, dp[bR][bC]] for bR, bC in baseCamp if arr[bR][bC] != -1]
        temp.sort(key=lambda x: (x[2], x[0], x[1]))
        bR, bC, _, = temp.pop(0)
        arr[bR][bC] = -1
        people[-1] = [people[-1][0], people[-1][1], people[-1][2], bR, bC]

    t += 1
    if not people and not pyeon:
        break

print(t)
