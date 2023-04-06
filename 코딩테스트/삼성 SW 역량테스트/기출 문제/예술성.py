# 1. 그룹화
# 2. 조화로움 계산
# 3. 십자 모양을 기준으로 반시계 방향 돌림
# 4. 십자 빼고 시계방향으로

from collections import deque

dR = [0, -1, 0, 1]
dC = [1, 0, -1, 0]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def notInRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return True
    return False

def grouping():
    group = []
    visited = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                group.append([[r, c]])
                q = deque()
                q.append([r, c])
                visited[r][c] = True
                target = arr[r][c]
                while q:
                    curR, curC, = q.popleft()
                    for i in range(4):
                        movedR, movedC = curR + dR[i], curC + dC[i]
                        if notInRange(movedR, movedC) or visited[movedR][movedC] or arr[movedR][movedC] != target:
                            continue
                        group[-1].append([movedR, movedC])
                        visited[movedR][movedC] = True
                        q.append([movedR, movedC])
    return group

def getNear(arr1, arr2):
    score = 0
    for r1, c1 in arr1:
        for r2, c2 in arr2:
            if abs(r1 - r2) + abs(c1 - c2) == 1:
                score += 1
    return score

def calc(group):
    score = 0
    for g1 in range(len(group) - 1):
        for g2 in range(g1 + 1, len(group)):
            g1R, g1C = group[g1][0]
            g2R, g2C = group[g2][0]
            tempScore = (len(group[g1]) + len(group[g2])) * arr[g1R][g1C] * arr[g2R][g2C] * getNear(group[g1], group[g2])
            score += tempScore
    return score

def rotate():
    newArr = [i[:] for i in arr]
    midR, midC = n // 2, n // 2

    # 십자 돌리기
    q = deque()
    for i in range(4):
        curR, curC = midR, midC
        while True:
            movedR, movedC = curR + dR[i], curC + dC[i]
            if notInRange(movedR, movedC):
                break
            q.append(arr[movedR][movedC])
            curR, curC = movedR, movedC

    for i in range(1, 5):
        curR, curC = midR, midC
        while True:
            movedR, movedC = curR + dR[i % 4], curC + dC[i % 4]
            if notInRange(movedR, movedC):
                break
            newArr[movedR][movedC] = q.popleft()
            curR, curC = movedR, movedC

    # 각자 돌리기
    for startR in range(0, n, n // 2 + 1):
        for startC in range(0, n, n // 2 + 1):
            # 역순으로 넣기
            temp = deque()
            for curC in range(startC, startC + n // 2):
                for curR in range(startR + n // 2 - 1, startR - 1, -1):
                    temp.append(arr[curR][curC])
            # 반영
            for curR in range(startR, startR + n // 2, 1):
                for curC in range(startC, startC + n // 2, 1):
                    newArr[curR][curC] = temp.popleft()

    return newArr

result = 0

group = grouping()
result += calc(group)
for _ in range(3):
    arr = rotate()
    group = grouping()
    result += calc(group)
print(result)