#   n x n 격자

#   팀
#   - 3명 이상이 한 팀
#   - 맨 앞 사람을 머리사람
#   - 맨 뒤 사람을 꼬리사람
#   - 선이 이어져있다

#   1. 각 팀은 머리사람을 따라서 한 칸 이동
#   2. 각 라운드 마다 공을 던진다
#   3. 공을 받으면 머리에서부터 n번 째면 n ** 2의 점수를 얻는다
#   - 공을 받은 팀은 머리와 꼬리가 바뀐다
from collections import deque

dR = [0, -1, 0, 1]
dC = [1, 0, -1, 0]

n, m, k, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
num = 0
team = {}

def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return False
    return True

def init():
    global num
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 1:
                visited = set()
                visited.add((r, c))
                team[num] = [[r, c]]
                q = deque([[r, c]])
                mid = 0
                while q:
                    curR, curC = q.popleft()
                    for i in range(4):
                        movedR, movedC = curR + dR[i], curC + dC[i]
                        if not inRange(movedR, movedC) or (movedR, movedC) in visited:
                            continue
                        if arr[movedR][movedC] == 0 or arr[movedR][movedC] == 4:
                            continue
                        if arr[movedR][movedC] == 3:
                            team[num].append([movedR, movedC])
                        visited.add((movedR, movedC))
                        q.append((movedR, movedC))
                        if arr[movedR][movedC] == 2:
                            mid += 1
                team[num].append(mid)
                num += 1

def move(arr):
    for num in team:
        head, tail, mid, = team[num]
        hR, hC, = head

        q = deque([1] + [2] * mid + [3])
        visited = set()
        while q:
            cur = q.popleft()
            if cur == 1:
                for i in range(4):
                    movedR, movedC = hR + dR[i], hC + dC[i]
                    if not inRange(movedR, movedC) or not (arr[movedR][movedC] == 3 or arr[movedR][movedC] == 4):
                        continue
                    arr[movedR][movedC] = cur
                    visited.add((movedR, movedC))
                    team[num][0] = [movedR, movedC]
                    break
            elif cur == 2:
                visited.add((hR, hC))
                arr[hR][hC] = cur
                for i in range(4):
                    movedR, movedC = hR + dR[i], hC + dC[i]
                    if not inRange(movedR, movedC) or (movedR, movedC) in visited or arr[movedR][movedC] == 0:
                        continue
                    hR, hC = movedR, movedC
                    break
            elif cur == 3:
                arr[hR][hC] = cur
                team[num][1] = [hR, hC]
                for i in range(4):
                    movedR, movedC = hR + dR[i], hC + dC[i]
                    if not inRange(movedR, movedC) or (movedR, movedC) in visited or arr[movedR][movedC] != 3:
                        continue
                    arr[movedR][movedC] = 4
                    break

def throw():
    d = (rud - 1) // n
    if d == 0:
        r, c = rud - 1, 0
    elif d == 1:
        r, c = n - 1, (rud - 1) % n
    elif d == 2:
        r, c = (n - 1 - (rud - 1) % n), n - 1
    else:
        r, c = 0, (n - 1 - (rud - 1) % n)

    for _ in range(n):
        if arr[r][c] == 0 or arr[r][c] == 4:
            r, c = r + dR[d], c + dC[d]
            continue
        return [r, c]
    return [-1, -1]

def getNum(r, c):
    if arr[r][c] == 1:
        return r, c, 1
    if arr[r][c] == 3:
        for num in team:
            if team[num][1] == [r, c]:
                return team[num][0][0], team[num][0][1], 1 + 1 + team[num][2]

    q = deque()
    q.append((r, c, 1))
    visited = set()
    visited.add((r, c))

    while q:
        curR, curC, diff = q.popleft()
        for i in range(4):
            movedR, movedC, = curR + dR[i], curC + dC[i]
            if not inRange(movedR, movedC) or (movedR, movedC) in visited:
                continue
            if arr[movedR][movedC] == 2:
                visited.add((movedR, movedC))
                q.append((movedR, movedC, diff + 1))
            elif arr[movedR][movedC] == 1:
                return movedR, movedC, diff + 1

init()
res = 0
for rud in range(1, k + 1):
    rud %= 4 * n
    if rud == 0:
        rud = 4 * n


    # 1
    move(arr)

    # 2
    temp = throw()
    if temp == [-1, -1]:
        continue
    sR, sC, diff, = getNum(temp[0], temp[1])
    res += diff ** 2
    for num in team:
        if team[num][0] == [sR, sC]:
            team[num][0], team[num][1] = team[num][1], team[num][0]
            arr[team[num][0][0]][team[num][0][1]] = 1
            arr[team[num][1][0]][team[num][1][1]] = 3
            break

print(res)