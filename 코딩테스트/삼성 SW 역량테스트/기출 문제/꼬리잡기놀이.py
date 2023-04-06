# TODO 틀림

# 1. 머리사람을 따라 한 칸 이동
# 2. 각 라운드마다 공을 던짐
#   [오, 위, 왼, 아] 순서로
# 3. 공을 맞은 사람이 머리를 기준으로 몇번째인지의 제곱을 res에 더함
import math
from collections import deque

dR = [0, -1, 0, 1]
dC = [1, 0, -1, 0]

def notInRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return True
    return False

n, m, k, = map(int, input().split())
first = [list(map(int, input().split())) for _ in range(n)]
team = []
visited = [[False] * n for _ in range(n)]
arr = [[-1] * n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if first[r][c] == 4:
            arr[r][c] = 0
        if first[r][c] == 1:
            team.append([[r, c, 1]])
            visited[r][c] = True
            arr[r][c] = len(team)

            q = deque()
            # 루프 검사
            loop = []
            for i in range(4):
                movedR, movedC = r + dR[i], c + dC[i]
                if notInRange(movedR, movedC):
                    continue
                loop.append(first[movedR][movedC])
            if 3 in loop:
                i = loop.index(2)
                movedR, movedC = r + dR[i], c + dC[i]
                visited[movedR][movedC] = True
                q.append([movedR, movedC, 2])
                arr[movedR][movedC] = len(team)
                team[-1].append([movedR, movedC, 2])
            else:
                # 루프 아니면
                q.append([r, c, 1])

            while q:
                curR, curC, num = q.popleft()
                for i in range(4):
                    movedR, movedC = curR + dR[i], curC + dC[i]
                    if notInRange(movedR, movedC) or visited[movedR][movedC]:
                        continue
                    if first[movedR][movedC] == 0 or first[movedR][movedC] == 4:
                        continue
                    team[-1].append([movedR, movedC, num + 1])
                    visited[movedR][movedC] = True
                    q.append([movedR, movedC, num + 1])
                    arr[movedR][movedC] = len(team)
                    break

result = 0
for round in range(k):

    # 이동
    for i in range(len(team)):
        r, c, num = team[i][0]
        for d in range(4):
            movedR, movedC = r + dR[d], c + dC[d]
            if notInRange(movedR, movedC) or arr[movedR][movedC] != 0:
                continue
            lastR, lastC, _ = team[i][-1]
            arr[lastR][lastC] = 0
            for j in range(len(team[i]) - 1, 0, -1):
                team[i][j][0], team[i][j][1] = team[i][j - 1][0], team[i][j - 1][1]
                arr[team[i][j][0]][team[i][j][1]] = i + 1
            team[i][0] = [movedR, movedC, num]
            arr[movedR][movedC] = i + 1
            break
        else:
            # maxD = math.inf
            # maxV = math.inf
            # for d in range(4):
            #     movedR, movedC = r + dR[d], c + dC[d]
            #     if notInRange(movedR, movedC):
            #         continue
            #     if arr[movedR][movedC] == i:
            #         for j in range(len(team[i])):
            #             if team[i][j][0] == movedR and team[i][j][1] == movedC:
            #                 if team[i][j][2] < maxV:
            #                     maxV = team[i][j][2]
            #                     maxD = d
            # nextFirstR, nextFistC = r + dR[maxD], c + dC[maxD]
            nextFirstR, nextFirstC, _ = team[i][-1]
            for j in range(len(team[i]) - 1, 0, -1):
                team[i][j][0], team[i][j][1] = team[i][j - 1][0], team[i][j - 1][1]
            team[i][0][0], team[i][0][1] = nextFirstR, nextFirstC

    # 공 던지기
    ballD = (round // n) % 4
    if ballD == 0:
        ballR, ballC = round % n, 0
    elif ballD == 1:
        ballR, ballC = n - 1, round % n
    elif ballD == 2:
        ballR, ballC = round % n, n - 1
    else:
        ballR, ballC = 0, round % n
    while True:
        # 만날 때까지 탐색
        movedR, movedC = ballR + dR[ballD], ballC + dC[ballD]
        if notInRange(movedR, movedC):
            break
        elif arr[movedR][movedC] == 0 or arr[movedR][movedC] == -1:
            ballR, ballC = movedR, movedC
            continue

        # 점수 추가
        teamNum = arr[movedR][movedC]
        for i in range(len(team[teamNum - 1])):
            curR, curC, num = team[teamNum - 1][i]
            if curR == movedR and curC == movedC:
                result += num ** 2
                break

        # 뒤집기
        team[teamNum - 1].reverse()
        for i in range(len(team[teamNum - 1])):
            team[teamNum - 1][i][-1] = i + 1
        break

print(result)