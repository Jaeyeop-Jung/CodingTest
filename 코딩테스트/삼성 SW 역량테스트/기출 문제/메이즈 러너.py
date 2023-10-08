# M명의 참가자가 미로 탈출
# 미로는 N X N
# 빈 칸 - 참가자가 이동 가능
# 벽 -이동할 수 없음, 1 ~ 9의 내구도를 가짐, 회전할 때 1씩 내구도가 깎임, 내구도가 0이 되면 빈칸
# 출구 참가자가 해당 칸에 도착하면 즉시 탈출

# 참가자는 동시에 움직임, 출구와 더 가까운 곳으로 이동,
#   움직일 수 있는 칸이 2개 이상이면 상하로 움직임
#   움직일 수 없으면 안움직임

#   움직임이 끝나면 출구와 참가자의 거리가 가장 가까운 애를 기준으로 작은 정사각형을 구함
#   좌상단 r이 작고, c좌표가 작은걸 우선으로
#   시계 방향으로 90도 회전하며, 회전된 벽은 내구도가 1깎임
from collections import deque

dR = [1, -1, 0, 0]
dC = [0, 0, 1, -1]
diagonalR = dR + [1, 1, -1, -1]
diagonalC = dC + [1, -1, -1, 1]

n, m, k, = map(int, input().split())
wall = [list(map(int, input().split())) for _ in range(n)]
arr = [[[] for _ in range(n)] for _ in range(n)]
member = {num: list(map(int, input().split())) for num in range(m)}
for num in member:
    r, c, = member[num]
    arr[r - 1][c - 1].append(num)
    member[num] = [r - 1, c - 1]
eR, eC = map(int, input().split())
eR, eC = eR - 1, eC - 1
arr[eR][eC].append(-1)

def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return False
    return True

def findMoveDirection(r, c):
    canMove = []
    curDiff = abs(eR - r) + abs(eC - c)
    for d in range(4):
        movedR, movedC = r + dR[d], c + dC[d]
        if not inRange(movedR, movedC):
            continue
        if curDiff <= abs(eR - movedR) + abs(eC - movedC) or 1 <= wall[movedR][movedC]:
            continue
        canMove.append(d)

    if not canMove:
        return -1
    canMove.sort()
    return canMove[0]

def getRectSize():
    q = deque()
    visited = [[False] * n for _ in range(n)]
    q.append((eR, eC, 0))
    visited[eR][eC] = True
    while q:
        r, c, diff, = q.popleft()
        for i in range(len(diagonalR)):
            movedR, movedC = r + diagonalR[i], c + diagonalC[i]
            if not inRange(movedR, movedC) or visited[movedR][movedC]:
                continue
            if arr[movedR][movedC]:
                return diff + 1
            q.append((movedR, movedC, diff + 1))
            visited[movedR][movedC] = True


def findRect():
    rectSize = getRectSize()
    for r in range(n - rectSize):
        for c in range(n - rectSize):
            for num in member:
                mR, mC = member[num]
                if (r <= mR < r + rectSize + 1 and c <= mC < c + rectSize + 1) and (r <= eR < r + rectSize + 1 and c <= eC < c + rectSize + 1):
                    return r, c, r + rectSize + 1, c + rectSize + 1
    return False

def rotate(arr, r1, c1, r2, c2):
    newWall = [i[:] for i in wall]
    newArr = [[i[:] for i in j] for j in arr]

    # 벽 돌리기
    oC = c1
    for r in range(r1, r2):
        q = deque()
        for cR in range(r2 - 1, r1 - 1, - 1):
            q.append(max(0, wall[cR][oC] - 1))
        for c in range(c1, c2):
            newWall[r][c] = q.popleft()
        oC += 1

    # 사람 돌리기
    oC = c1
    for r in range(r1, r2):
        q = deque()
        for oR in range(r2 - 1, r1 - 1, - 1):
            q.append(arr[oR][oC][:])
        for c in range(c1, c2):
            newArr[r][c] = q.popleft()
            for num in newArr[r][c]:
                if num == -1:
                    global eR, eC
                    eR, eC = r, c
                else:
                    member[num] = [r, c]
        oC += 1
    return newWall, newArr

res = 0
for _ in range(k):
    if not member:
        break

    # 움직이기
    finish = []
    for num in member:
        curR, curC, = member[num]
        direction = findMoveDirection(curR, curC)
        if direction == -1:
            continue
        movedR, movedC = curR + dR[direction], curC + dC[direction]
        arr[curR][curC].remove(num)
        res += 1
        if movedR == eR and movedC == eC:
            finish.append(num)
            continue
        arr[movedR][movedC].append(num)
        member[num] = [movedR, movedC]
    for num in finish:
        del member[num]

    if not member:
        break

    # 회전하기
    rect = findRect()
    r1, c1, r2, c2 = rect
    wall, arr = rotate(arr, r1, c1, r2, c2)

print(res)
print(eR + 1, eC + 1)