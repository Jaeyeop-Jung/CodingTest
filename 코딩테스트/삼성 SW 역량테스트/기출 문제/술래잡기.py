#   1. 술래와 거리가 3이하인 도망자만 움직임
#   2. 움직였을 때 격자를 벗어나지 않으면
#       - 움직이는 칸에 술래 있으면 X
#      격자를 벗어나면
#       - 방향을 반대로 틀고, 술래가 없으면 움직임
#   3. 술래가 움직임
#       이동 후에 방향이 틀어지는 곳이면 즉시 튼다
#       끝점인 경우도 바로 튼다
#   4. 시야 방향으로 3칸에 있는 술래를 잡는다
#       나무가 있는 칸은 가려져서 안보이니까 넘긴다
#       result += 현재턴 * 현재 턴에서 잡힌 도망자 수
#       도망자는 사라진다

dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]
WOOD = -1

n, m, h, k, = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
runner = {}
for num in range(m):
    x, y, d = map(int, input().split())
    if d == 1:
        runner[num] = [x - 1, y - 1, 1]
    else:
        runner[num] = [x - 1, y - 1, 2]
    arr[x - 1][y - 1].append(num)
for _ in range(h):
    x, y = map(int, input().split())
    arr[x - 1][y - 1].append(WOOD)
catcherR, catcherC = n // 2, n // 2
catcherD = 0
catcherMove = 0     # 이동 횟수
catcherCurMoveCnt = 1   # 현재 사이클의 최대 이동 횟수
catcherMoveCnt = 0  # 2가 되면 catcherCurMoveCnt + 1
catcherTurnCnt = 0  # catcherCurMoveCnt와 같아지면 방향 꺾기
back = False
result = 0

def notInRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return True
    return False

def runnerRun():
    for runnerNum in runner:
        r, c, d = runner[runnerNum]
        if 3 < abs(catcherR - r) + abs(catcherC - c) or notInRange(r, c):
            continue
        movedR, movedC = r + dR[d], c + dC[d]
        if notInRange(movedR, movedC):
            d = (d + 2) % 4
            runner[runnerNum][-1] = d
            movedR, movedC = r + dR[d], c + dC[d]
        if movedR == catcherR and movedC == catcherC:
            continue
        arr[r][c].remove(runnerNum)
        arr[movedR][movedC].append(runnerNum)
        runner[runnerNum] = [movedR, movedC, d]

def moveCatcher():
    global catcherR, catcherC, catcherD, catcherMove, catcherMoveCnt, catcherTurnCnt, catcherCurMoveCnt, back
    catcherR, catcherC = catcherR + dR[catcherD], catcherC + dC[catcherD]
    if catcherR == n - 1 and catcherC == 0:
        catcherMoveCnt -= 1
    if not back:
        catcherMove += 1
        if catcherMove == catcherCurMoveCnt:
            catcherMoveCnt += 1
            catcherMove = 0
            catcherD = (catcherD + 1) % 4
        if catcherMoveCnt == 2: # 2사이클이 돌아서 +1 해야함
            catcherCurMoveCnt += 1
            catcherMoveCnt = 0
        if catcherR == 0 and catcherC == 0: # 끝 점이면
            catcherD = (catcherD + 1) % 4
            catcherCurMoveCnt -= 1
            back = True
    else:
        catcherMove += 1
        if catcherMove == catcherCurMoveCnt:
            catcherMoveCnt += 1
            catcherMove = 0
            catcherD = (catcherD - 1) % 4
        if catcherMoveCnt == 2: # 2사이클이 돌아서 -1 해야함
            catcherCurMoveCnt -= 1
            catcherMoveCnt = 0
        if catcherR == n // 2 and catcherC == n // 2: # 끝 점이면
            catcherD = (catcherD - 1) % 4
            catcherCurMoveCnt += 1
            back = False

def catch():
    global result
    curR, curC = catcherR, catcherC
    cnt = 0
    if arr[curR][curC] and -1 not in arr[curR][curC]:
        for runnerNum in arr[curR][curC]:
            cnt += 1
            del runner[runnerNum]
        arr[curR][curC] = []
    for _ in range(2):
        movedR, movedC = curR + dR[catcherD], curC + dC[catcherD]
        if notInRange(movedR, movedC):
            break
        if arr[movedR][movedC] and -1 not in arr[movedR][movedC]:
            for runnerNum in arr[movedR][movedC]:
                cnt += 1
                del runner[runnerNum]
            arr[movedR][movedC] = []
        curR, curC = movedR, movedC
    result += turn * cnt

for turn in range(1, k + 1):
    runnerRun()
    moveCatcher()
    catch()

print(result)
