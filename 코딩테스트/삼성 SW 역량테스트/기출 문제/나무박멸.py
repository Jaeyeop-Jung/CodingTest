# TODO 틀림 더 꼼꼼히 구현

# 제초제는 k의 범위만큼 대각선으로 퍼지고, 벽이 있으면 안됌
# 1. 나무가 인접한 4칸에 나무가 있는 개수만큼 성장함
# 2. 나무가 벽, 다른 나무, 제초제가 없는 칸에 번식을한다
#       int(나무의 성장력 / 빈 칸)으로 번식. 합해야함
# 3. 나무가 있는 칸에 제초제를 뿌린다.
#       빈 칸이나 벽이면 거기까지 뿌려지고 멈춤
#       제초제가 뿌려진 칸은 c년만큼 제초제가 살아있음
#       제초제가 있는데 또 제초제를 뿌리면 c년 동안 유지
#       가장 많이 나무를 죽이는 곳으로 뿌리는데, 여러개면 행이작고, 열이 작은 곳으로

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

diagonalR = [1, 1, -1, -1]
diagonalC = [1, -1, -1, 1]

WALL = -1
EMPTY = 0

n, m, k, cancel, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
terArr = [[0] * n for _ in range(n)]

def notInRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return True
    return False

def grow():
    global arr
    for r in range(n):
        for c in range(n):
            if 0 < arr[r][c]:
                cnt = 0
                for i in range(4):
                    movedR, movedC = r + dR[i], c + dC[i]
                    if notInRange(movedR, movedC) or arr[movedR][movedC] <= 0:
                        continue
                    cnt += 1
                arr[r][c] += cnt

def expand():
    newArr = [i[:] for i in arr]
    for r in range(n):
        for c in range(n):
            if 0 < arr[r][c]:
                available = []
                for i in range(4):
                    movedR, movedC = r + dR[i], c + dC[i]
                    if notInRange(movedR, movedC):
                        continue
                    if arr[movedR][movedC] == EMPTY and terArr[movedR][movedC] == 0:
                        available.append([movedR, movedC])

                if len(available) == 0:
                    continue
                expandLife = int(arr[r][c] / len(available))
                for expandR, expandC in available:
                    newArr[expandR][expandC] += expandLife
    return newArr

def terminate():
    # 최대 피해 지역 찾기
    targetR, targetC = n, n
    terminateNum = 0
    for r in range(n - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            if arr[r][c] == EMPTY:
                if terminateNum == 0:
                    targetR, targetC = r, c
            elif 0 < arr[r][c]:
                total = arr[r][c]
                for i in range(4):
                    curR, curC = r, c
                    for _ in range(k):
                        movedR, movedC = curR + diagonalR[i], curC + diagonalC[i]
                        if notInRange(movedR, movedC):
                            break
                        if arr[movedR][movedC] == WALL or arr[movedR][movedC] == EMPTY:
                            break
                        total += arr[movedR][movedC]
                        curR, curC = movedR, movedC
                if terminateNum <= total:
                    targetR, targetC = r, c
                    terminateNum = total

    # 뿌리기
    global result
    result += arr[targetR][targetC]
    arr[targetR][targetC] = 0
    terArr[targetR][targetC] = cancel
    for i in range(4):
        curR, curC = targetR, targetC
        for _ in range(k):
            movedR, movedC = curR + diagonalR[i], curC + diagonalC[i]
            if notInRange(movedR, movedC):
                break
            if arr[movedR][movedC] == EMPTY or arr[movedR][movedC] == WALL:
                terArr[movedR][movedC] = cancel
                break
            result += arr[movedR][movedC]
            arr[movedR][movedC] = 0
            terArr[movedR][movedC] = cancel
            curR, curC = movedR, movedC

def timeout():
    for r in range(n):
        for c in range(n):
            if 0 < terArr[r][c]:
                terArr[r][c] -= 1

for _ in range(m):
    grow()
    arr = expand()
    timeout()
    terminate()


print(result)