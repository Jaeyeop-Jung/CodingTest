#   N x M 격자에 모든 위치에는 포탑이 있다

#   포탑
#   - 공격력이 존재
#   - 상황에따라 공격력이 줄거나 늘어날 수 있다
#   - 공격력이 0이되면 포탑은 부서져 공격을 못함
#   - 처음부터 0도 있다

#   1. 가장 약한 포탑의 공격력이 N + M만큼 증가한다
#   - 공격력이 가장 낮고, 2개 이상이면 가장 최근에 공격한 포탑, 행과 열의 합이 큰 포탑, 열 값이 큰 포탑
#   2. 선정된 가장 약한 포탑이 자신을 제외한 가장 강한 포탑을 공격
#   - 공격력이 가장 높은 포탑, 공격한지 가장 오래 된, 행과 열의 합이 작고, 열이 작은 포탑
#   2-1. 레이저 공격
#   - 부서진 포탑은 못지나간다
#   - 범위를 벗어나면 반대편으로 나온다
#   - 경로가 여러개면 사전순으로 빠른게 우선
#   - 경로에 있는 애들은 나누기 2만큼 공격을 받는다
#   2-2. 포탄 공격
#   - 공격 대상는 공격력만큼, 주위 8방향은 나누기 2만큼 피해를 받는다
#   - 공격자는 데미지를 받지 않음
#   - 범위를 넘으면 반대편이 맞는다
#   3. 포탑의 공격력이 0이하가 되면 포탑이 부서짐
#   4. 공격자 X and 공격 대상 X면 공격력이 1 오른다
import math
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]
diagonalR = [0, 1, 1, 1, 0, -1, -1, -1]
diagonalC = [1, 1, 0, -1, -1, -1, 0, 1]

n, m, k, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
recent = [[0] * m for _ in range(n)]

def findWeaker():
    minAttack = math.inf
    turret = []
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 0:
                continue
            if arr[r][c] < minAttack:
                minAttack = arr[r][c]
                turret = [(r, c)]
            elif arr[r][c] == minAttack:
                turret.append((r, c))
    turret.sort(key=lambda x: (-recent[x[0]][x[1]], -sum(x), -x[1]))
    return turret[0][0], turret[0][1]

def findStronger():
    maxAttack = -1
    turret = []
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 0 or (sR == r and sC == c):
                continue
            if maxAttack < arr[r][c]:
                maxAttack = arr[r][c]
                turret = [(r, c)]
            elif arr[r][c] == maxAttack:
                turret.append((r, c))
    turret.sort(key=lambda x: (recent[x[0]][x[1]], sum(x), x[1]))
    return turret[0][0], turret[0][1]

def findPath(sR, sC, eR, eC):
    q = deque()
    visited = [[False] * m for _ in range(n)]
    visited[sR][sC] = True
    q.append([sR, sC, []])
    while q:
        curR, curC, path, = q.popleft()
        for i in range(4):
            movedR, movedC = (curR + dR[i]) % n, (curC + dC[i]) % m
            if visited[movedR][movedC] or arr[movedR][movedC] == 0:
                continue
            if movedR == eR and movedC == eC:
                return path + [[eR, eC]]
            visited[movedR][movedC] = True
            newPath = [i[:] for i in path]
            newPath.append((movedR, movedC))
            q.append([movedR, movedC, newPath])
    return []

def lazerAttack(sR, sC, eR, eC):
    path = findPath(sR, sC, eR, eC)
    if not path:
        return False
    for i in range(len(path) - 1):
        r, c = path[i]
        arr[r][c] -= arr[sR][sC] // 2
        if arr[r][c] <= 0:
            arr[r][c] = 0
        relation.add((r, c))
    arr[eR][eC] -= arr[sR][sC]
    if arr[eR][eC] <= 0:
        arr[eR][eC] = 0
    return True

def shootAttack(sR, sC, eR, eC):
    for i in range(8):
        r, c = (eR + diagonalR[i]) % n, (eC + diagonalC[i]) % m
        if r == sR and c == sC:
            continue
        relation.add((r, c))
        arr[r][c] -= arr[sR][sC] // 2
        if arr[r][c] <= 0:
            arr[r][c] = 0
    arr[eR][eC] -= arr[sR][sC]
    if arr[eR][eC] <= 0:
        arr[eR][eC] = 0

for rud in range(1, k + 1):
    cnt = 0
    for r in range(n):
        for c in range(m):
            if 0 < arr[r][c]:
                cnt += 1
    if cnt == 1:
        break

    # 1
    sR, sC = findWeaker()
    arr[sR][sC] += n + m

    # 2
    eR, eC = findStronger()
    relation = set([(sR, sC), (eR, eC)])
    if not lazerAttack(sR, sC, eR, eC):
        shootAttack(sR, sC, eR, eC)

    # 3 0이하 포탑이 부서지고, recent 업데이트
    recent[sR][sC] = rud
    cnt = 0
    for r in range(n):
        for c in range(m):
            if 0 < arr[r][c]:
                cnt += 1
    if cnt == 1:
        break

    # 4
    for r in range(n):
        for c in range(m):
            if (r, c) not in relation and arr[r][c] != 0:
                arr[r][c] += 1

print(max(map(max, arr)))