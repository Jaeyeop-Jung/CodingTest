#   검은색, 무지개, 일반 블록이 있다
#   일반 블록은 M까지의 숫자 중 하나다
#   검은색 블록은 -1이다
#   무지개 블록은 0이다

#   블록 그룹
#   - 블록의 개수는 2이상이며, 모든 블록은 연결되어 있어야함
#   - 그룹의 기준은 일반 블록에서 행의 번호가 가장 작고, 열의 번호가 작은 것이다
#   - 일반 블록이 적어도 하나 있어야함
#   - 무지개 블록은 얼마든 상관없고
#   - 검은색 블록은 X

#   중력
#   - 검은색 블록은 중력이 작용하지 않는다

#   플레이
#   1. 크기가 가장 큰 블록을 찾는다.
#   - 무지개 블록 수가 많고, 기준 블록의 행이 가장 큰 거, 열이 가장 큰 거
#   2. 블록을 제거하고, 블록의 갯수 B^2의 점을 흭득한다
#   3. 중력 작용
#   4. 90도 반시계로 돌린다
#   5. 중력 작용
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

EMPTY = -2
BLACK = -1
RAINBOW = 0

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def rotate(arr):
    newArr = [[0] * n for _ in range(n)]
    for r in range(n):
        q = deque()
        for curR in range(n - 1, -1, -1):
            q.append(arr[curR][n - r - 1])
        for c in range(n - 1, -1, -1):
            newArr[r][c] = q.popleft()
    return newArr

def gravity(arr):
    newArr = [[EMPTY] * n for _ in range(n)]
    for c in range(n):
        q = deque()
        putR = n - 1
        for r in range(n - 1, -1, -1):
            if arr[r][c] == BLACK:
                while q:
                    newArr[putR][c] = q.popleft()
                    putR -= 1
                newArr[r][c] = BLACK
                putR = r - 1
            elif arr[r][c] != EMPTY:
                q.append(arr[r][c])
        while q:
            newArr[putR][c] = q.popleft()
            putR -= 1
    return newArr

def find():
    group = []
    for r in range(n):
        for c in range(n):
            if 1 <= arr[r][c]:
                visited = [[False] * n for _ in range(n)]
                q = deque([(r, c)])
                generalBlock = [[r, c]]
                rainbowCnt = 0
                visited[r][c] = True

                while q:
                    curR, curC, = q.popleft()
                    for i in range(len(dR)):
                        movedR, movedC = curR + dR[i], curC + dC[i]
                        if not 0 <= movedR < n or not 0 <= movedC < n:
                            continue
                        if visited[movedR][movedC] or arr[movedR][movedC] <= -1:
                            continue

                        if arr[movedR][movedC] == 0 or arr[movedR][movedC] == arr[r][c]:
                            if arr[movedR][movedC] == 0:
                                rainbowCnt += 1
                            else:
                                generalBlock.append([movedR, movedC])
                            q.append((movedR, movedC))
                            visited[movedR][movedC] = True

                if 1 <= len(generalBlock) and 2 <= len(generalBlock) + rainbowCnt:
                    generalBlock.sort(key=lambda x: (x[0], x[1]))
                    group.append([generalBlock, rainbowCnt])
    return group

def remove(r, c):
    q = deque()
    q.append((r, c))
    visited = [[False] * n for _ in range(n)]
    visited[r][c] = True
    cur = arr[r][c]
    arr[r][c] = EMPTY
    cnt = 1
    while q:
        curR, curC, = q.popleft()
        for i in range(len(dR)):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if visited[movedR][movedC] or arr[movedR][movedC] <= -1:
                continue
            if arr[movedR][movedC] == 0 or arr[movedR][movedC] == cur:
                arr[movedR][movedC] = EMPTY
                cnt += 1
                visited[movedR][movedC] = True
                q.append((movedR, movedC))
    return cnt

res = 0
while True:
    # 모든 그룹 찾기
    group = find()
    if not group:
        break

    # 가장 큰 그룹 찾기
    group.sort(key=lambda x: (-(len(x[0]) + x[1]), -x[1], -x[0][0][0], -x[0][0][1]))
    generalBlock, rainbowCnt = group[0]

    # 블록 제거하고 점수 얻기
    res += remove(generalBlock[0][0], generalBlock[0][1]) ** 2

    # 중력
    arr = gravity(arr)

    # 90도 돌리기
    arr = rotate(arr)

    # 중력
    arr = gravity(arr)

print(res)