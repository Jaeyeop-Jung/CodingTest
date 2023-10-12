#   N x N 격자
#   마법사 상어는 (N + 1) // 2, (N + 1) // 2에 있다
#   달팽이 모양으로 번호가 매겨져있다
#   위, 아래, 왼쪽, 오른쪽의 정수 1, 2, 3, 4로 나타낸다

#   1. 상어가 방향으로 공격을 해 빈 칸으로 만든다
#   2. 구슬이 채워 진다
#   3. 구슬이 4개 이상 연속될 경우 폭발한다
#   4. 구슬이 채워 진다
#   5. 3번을 반복하며 더 이상 폭발할 구슬이 없으면 멈춘다
#   6. 구슬을 그룹으로 묵는다
#   - [갯수, 구슬의 번호]로 바뀌고 이를 놓는다
#   - 칸이 넘으면 그 구슬은 버린다

from collections import deque

dR = [-1, 1, 0, 0]
dC = [0, 0, -1, 1]
mR = [0, 1, 0, -1]
mC = [-1, 0, 1, 0]

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return False
    return True

def attack():
    r, c = n // 2, n // 2
    for _ in range(s):
        r, c = r + dR[d], c + dC[d]
        arr[r][c] = 0

def pull(arr):
    newArr = [[0] * n for _ in range(n)]

    # 큐에 넣기
    q = deque()
    r, c = n // 2, n // 2
    moveCnt = 1
    d = 0
    while True:
        flag = False
        for _ in range(2):
            for _ in range(moveCnt):
                r, c = r + mR[d], c + mC[d]
                if not inRange(r, c):
                    flag = True
                    break
                if arr[r][c] == 0:
                    continue
                q.append(arr[r][c])
            if flag:
                break
            d = (d + 1) % 4
        if flag:
            break
        moveCnt += 1

    # 큐에서 빼서 newArr에 집어넣기
    r, c = n // 2, n // 2
    moveCnt = 1
    d = 0
    while True:
        flag = False
        for _ in range(2):
            for _ in range(moveCnt):
                r, c = r + mR[d], c + mC[d]
                if not inRange(r, c) or not q:
                    flag = True
                    break
                newArr[r][c] = q.popleft()
            if flag:
                break
            d = (d + 1) % 4
        if flag:
            break
        moveCnt += 1

    return newArr

def changeToZero(coord):
    for r, c in coord:
        arr[r][c] = 0

def explosion():
    global res

    r, c = n // 2, n // 2
    moveCnt = 1
    d = 0
    cur = 0
    exp = []
    temp = False
    while True:
        flag = False
        for _ in range(2):
            for _ in range(moveCnt):
                r, c = r + mR[d], c + mC[d]
                if not inRange(r, c) or arr[r][c] == 0:
                    flag = True
                    if 4 <= len(exp):
                        changeToZero(exp)
                        res[cur - 1] += len(exp)
                        temp = True
                    break

                if cur == arr[r][c]:
                    exp.append((r, c))
                else:
                    if 4 <= len(exp):
                        changeToZero(exp)
                        res[cur - 1] += len(exp)
                        temp = True
                    cur = arr[r][c]
                    exp = [(r, c)]
            if flag:
                break
            d = (d + 1) % 4
        if flag:
            break
        moveCnt += 1
    return temp

def change(arr):
    newArr = [[0] * n for _ in range(n)]

    # 큐에 넣기
    q = deque()
    r, c = n // 2, n // 2
    moveCnt = 1
    d = 0
    cur = 0
    cnt = 0
    while True:
        flag = False
        for _ in range(2):
            for _ in range(moveCnt):
                r, c = r + mR[d], c + mC[d]
                if not inRange(r, c) or arr[r][c] == 0:
                    flag = True
                    q.append(cnt)
                    q.append(cur)
                    break

                if cur == arr[r][c]:
                    cnt += 1
                else:
                    q.append(cnt)
                    q.append(cur)
                    cur = arr[r][c]
                    cnt = 1

            if flag:
                break
            d = (d + 1) % 4
        if flag:
            break
        moveCnt += 1

    # 큐에서 빼서 newArr에 집어넣기
    q.popleft()
    q.popleft()
    r, c = n // 2, n // 2
    moveCnt = 1
    d = 0
    while True:
        flag = False
        for _ in range(2):
            for _ in range(moveCnt):
                r, c = r + mR[d], c + mC[d]
                if not inRange(r, c) or not q:
                    flag = True
                    break
                newArr[r][c] = q.popleft()
            if flag:
                break
            d = (d + 1) % 4
        if flag:
            break
        moveCnt += 1

    return newArr


res = [0, 0, 0]
for _ in range(m):
    d, s = map(int, input().split())
    d -= 1

    # 1
    attack()

    # 2
    arr = pull(arr)

    # 3, 4, 5
    while explosion():
        arr = pull(arr)

    # 6
    arr = change(arr)

print(res[0] + res[1] * 2 + res[2] * 3)