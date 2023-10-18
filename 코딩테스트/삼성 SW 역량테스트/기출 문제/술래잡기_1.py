#   n x n 격자
#   m명의 도망자가 있다

#   술래
#   - 처음엔 정중앙에 있다

#   도망자
#   - 좌우 또는 상하 로만 움직이는 유형이 있다
#   - 좌우로 움직이는 유형은 항상 오른쪽을 보고
#   - 상하로만 움직이는 유형은 아래쪽을 본다

#   1. 술래와 거리가 3이하인 도망자가 동시에 움직인다
#   2-1. 바라보는 방향으로 움직이는데 격자 안이면
#   - 움직이려는 칸에 술래가 있으면 움직이지 않는다
#   - 없으면 움직인다
#   2-2. 겪자를 벗어나면
#   - 방향을 반대로 틀고 술래가 없다면 움직인다
#   3. 술래가 움직인다
#   - 달팽이 방향으로 움직인다
#   - 움직인 방향에서 방향을 틀어야되면 즉시 방향을 변경한다(끝이나 정중아도 마찬가지다)
#   4. 술래의 시야에 3칸 이내에 잇는 도망자를 잡는다. 나무가 있는 칸은 도망자가 안잡힌다
#   - 술래가 있는 칸을 포함해 3칸이내
#   - 잡힌 도망자는 사라진다
#   - 현재 턴 x 현재 턴에서 잡힌 도망자의 수 만큼 점수를 얻는다

dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]

n, m, h, k, = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
player = {}
for num in range(m):
    r, c, d = map(int, input().split())
    arr[r - 1][c - 1].append(num)
    if d == 1:
        player[num] = [r - 1, c - 1, d, 1]
    elif d == 2:
        player[num] = [r - 1, c - 1, d, 2]
for _ in range(h):
    r, c = map(int, input().split())
    arr[r - 1][c - 1].append(-1)

def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return False
    return True

def findRunPlayer(r, c):
    runner = []
    for num in player:
        playerR, playerC, d, t = player[num]
        if abs(r - playerR) + abs(c - playerC) <= 3:
            runner.append(num)
    return runner

def move(r, c, runner):
    for num in runner:
        playerR, playerC, d, t = player[num]
        movedR, movedC = playerR + dR[d], playerC + dC[d]
        if not inRange(movedR, movedC):
            d = (d + 2) % 4
            player[num] = [playerR, playerC, d, t]
            movedR, movedC = playerR + dR[d], playerC + dC[d]

        if movedR == r and movedC == c:
            continue
        player[num] = [movedR, movedC, d, t]
        arr[playerR][playerC].remove(num)
        arr[movedR][movedC].append(num)

def catcherMove():
    global catcherR, catcherC, catcherD, curMaxMoveCnt, rotateDirectionCnt, moveCnt, moveFlag

    # 움직이기
    catcherR, catcherC = catcherR + dR[catcherD], catcherC + dC[catcherD]
    moveCnt += 1

    # 최대 움직임 수끼지 움직였을 때(방향 바꾸기, 최대 움직임 수 수정 등)
    if moveCnt == curMaxMoveCnt:
        rotateDirectionCnt += 1
        moveCnt = 0
        # 가장 바깥을 돌 때
        if curMaxMoveCnt == n - 1 and rotateDirectionCnt == 3:
            # 정방향이면 맨 끝에 도착했을 때
            if moveFlag:
                catcherD = (catcherD + 2) % 4
                moveFlag ^= True
            # 역방향이면 1만 돌린다
            else:
                catcherD = (catcherD - 1) % 4
                curMaxMoveCnt -= 1
            rotateDirectionCnt = 0

        # 가장 바깥이 아닐 때
        elif curMaxMoveCnt != n - 1 and rotateDirectionCnt == 2:
            # 정방향 일 때
            if moveFlag:
                catcherD = (catcherD + 1) % 4
                curMaxMoveCnt += 1
            # 역방향 일 때
            else:
                catcherD = (catcherD - 1) % 4
                curMaxMoveCnt -= 1

                # 역방향이고, 맨 끝에 도착했으면
                if not moveFlag and curMaxMoveCnt == 0:
                    curMaxMoveCnt = 1
                    catcherD = (catcherD - 1) % 4
                    moveFlag ^= True
            rotateDirectionCnt = 0

        # 방향만 틀기
        else:
            # 정방향 일 때
            if moveFlag:
                catcherD = (catcherD + 1) % 4
            else:
                catcherD = (catcherD - 1) % 4

def catch():
    global catcherR, catcherC, catcherD, res
    curR, curC = catcherR, catcherC
    for _ in range(3):
        if -1 in arr[curR][curC]:
            curR, curC = curR + dR[catcherD], curC + dC[catcherD]
            if not inRange(curR, curC):
                break
            continue
        for num in arr[curR][curC]:
            del player[num]
        res += len(arr[curR][curC]) * rud
        arr[curR][curC] = []
        curR, curC = curR + dR[catcherD], curC + dC[catcherD]
        if not inRange(curR, curC):
            break


res = 0
catcherR, catcherC = n // 2, n // 2
catcherD = 0
curMaxMoveCnt = 1
rotateDirectionCnt = 0
moveCnt = 0
moveFlag = True
for rud in range(1, k + 1):
    # 1
    runner = findRunPlayer(catcherR, catcherC)

    # 2
    move(catcherR, catcherC, runner)

    # 3
    catcherMove()

    # 4
    catch()

print(res)