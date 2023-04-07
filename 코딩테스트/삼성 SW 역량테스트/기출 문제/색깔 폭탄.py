#   1. 가장 큰 폭탄 묶음을 찾는다
#       모두 같은 색깔로 이루어진 폭탄 or (빨간색 폭탄으로만 이루어지지 않고 and 빨간색 폭탄을 포함해 2개의 색깔로만)
#   2. 크기가 가장 큰 폭탄 묶음을 고른다
#       1. 가장 많은 수의 폭탄
#       2. 빨간색 폭탄이 가장 적게 포함된 것
#       3. 폭탄 묶음의 기준이 가장 큰 행, 가장 작은 열
#   3. 폭탄 제거 후 중력 작용. 돌은 이동하지 않음
#   4. 반시계 방향으로 회전
#   5. 중력 작용
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]
EMPTY = -2
BLACK = -1
RED = 0

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def notInRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return True
    return False


def findBomb():
    bomb = []
    for r in range(n):
        for c in range(n):
            if 0 < arr[r][c]:
                visited = [[False] * n for _ in range(n)]
                q = deque()
                q.append([r, c])
                color = arr[r][c]
                visited[r][c] = True
                redCnt = 0
                temp = [[r, c, color]]
                while q:
                    curR, curC, = q.popleft()
                    for i in range(4):
                        movedR, movedC = curR + dR[i], curC + dC[i]
                        if notInRange(movedR, movedC) or arr[movedR][movedC] == BLACK or arr[movedR][movedC] == EMPTY or visited[movedR][movedC]:
                            continue
                        if 0 < arr[movedR][movedC] and arr[movedR][movedC] != color:
                            continue
                        if arr[movedR][movedC] == RED:
                            redCnt += 1
                            temp.append([movedR, movedC, RED])
                        else:
                            temp.append([movedR, movedC, color])
                        q.append([movedR, movedC])
                        visited[movedR][movedC] = True
                if 2 <= len(temp):
                    bomb.append([redCnt, temp])
    return bomb

def findMaxBomb(bombGroup):
    for cnt, group in bombGroup:
        group.sort(key=lambda x: (-x[2], -x[0], x[1]))
    bombGroup.sort(key=lambda x: (-len(x[1]), x[0], -x[1][0][0], x[1][0][1]))
    return bombGroup[0]

def gravity():
    newArr = [[EMPTY] * n for _ in range(n)]
    for c in range(n):
        stack = []
        for r in range(n):
            if arr[r][c] == EMPTY:
                continue
            if arr[r][c] == BLACK:
                newArr[r][c] = BLACK
                nextR = r - 1
                while stack:
                    newArr[nextR][c] = stack.pop()
                    nextR -= 1
            else:
                stack.append(arr[r][c])
        if stack:
            nextR = n - 1
            while stack:
                newArr[nextR][c] = stack.pop()
                nextR -= 1
    return newArr

def rotate():
    newArr = [i[:] for i in arr]
    temp = deque()
    for c in range(n - 1, -1, -1):
        for r in range(n):
            temp.append(arr[r][c])
    for r in range(n):
        for c in range(n):
            newArr[r][c] = temp.popleft()
    return newArr

result = 0
while True:
    bombGroup = findBomb()
    if len(bombGroup) == 0:
        break
    maxBombGroup = findMaxBomb(bombGroup)
    result += len(maxBombGroup[1]) ** 2
    for i in range(len(maxBombGroup[1])):
        r, c, _, = maxBombGroup[1][i]
        arr[r][c] = EMPTY

    arr = gravity()
    arr = rotate()
    arr = gravity()

print(result)