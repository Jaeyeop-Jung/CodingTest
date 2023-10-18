#   n x n 격자
#   격자에는 1 ~ 6까지의 숫자가 그려져 있다
#   마주보고 있는 숫자의 합은 7이다

#   움직임
#   - 처음에는 항상 오른쪽으로 움직인다
#   1. 주사위가 방향대로 움직인다
#   - 격자 밖으로 벗어나면 방향이 반대로 된 뒤에 한 칸 움직인다
#   2. 주사위 면 업데이트
#   3. 해당 격자판 위의 점수와 상하좌우로 인접한 점수의 합을 얻는다
#   4-1. 격자의 칸 < 주사위의 아래면이면 시계방향으로 90도 회전
#   4-2. 주사위의 아래면 < 격자의 칸이면 반시계방향으로 90도 회전
#   4-3. 같다면 그대로 진행

from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dice = [1, 3, 2, 4, 5, 6]

def changeDice(d):
    if d == 0:
        dice[0], dice[1], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[1]
    elif d == 1:
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[2]
    elif d == 2:
        dice[0], dice[1], dice[3], dice[5] = dice[1], dice[5], dice[0], dice[3]
    else:
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[5], dice[0], dice[4]

def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return False
    return True

def bfs(r, c):
    visited = [[False] * n for _ in range(n)]
    visited[r][c] = True
    q = deque([(r, c)])
    target = arr[r][c]
    cnt = 1
    while q:
        curR, curC = q.popleft()
        for i in range(4):
            movedR, movedC = curR + dR[i], curC + dC[i]
            if not inRange(movedR, movedC) or visited[movedR][movedC]:
                continue
            if arr[movedR][movedC] != target:
                continue
            cnt += 1
            visited[movedR][movedC] = True
            q.append((movedR, movedC))
    return cnt

res = 0
r, c, d = 0, 0, 0
for _ in range(m):

    # 1
    movedR, movedC = r + dR[d], c + dC[d]
    if not inRange(movedR, movedC):
        d = (d + 2) % 4
        movedR, movedC = r + dR[d], c + dC[d]

    # 2
    changeDice(d)
    r, c = movedR, movedC

    # 3
    res += bfs(r, c) * arr[r][c]

    # 4
    if arr[r][c] < dice[-1]:
        d = (d + 1) % 4
    elif dice[-1] < arr[r][c]:
        d = (d - 1) % 4

print(res)