# 상어 위치는 가운데, 달팽이
# 1. 블리자드 마법 방향 [위, 아래, 왼, 오], 거리 s 파괴
# 2. 구슬 빈 칸으로 이동
# 3. 구슬 폭발. 달팽이로 연속하는 구슬 4개 이상이면 폭발
# 4. 구슬 빈 칸으로 이동
# 5. 연속하는 구슬은 '그룹'. 이 그룹은 [구슬 번호, 구슬 개수]로 칸을 2개로 변경
#       범위를 초과하면 구슬 사라짐
#
# return 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)

dR = [-1, 1, 0, 0]
dC = [0, 0, -1, 1]

mR = [0, 1, 0, -1]
mC = [-1, 0, 1, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
magics = [list(map(int, input().split())) for _ in range(m)]
sharkR, sharkC = (n + 1) // 2 - 1, (n + 1) // 2 - 1

def 파괴():
    curR, curC = sharkR, sharkC
    for _ in range(s):
        movedR, movedC = curR + dR[d - 1], curC + dC[d - 1]
        if not 0 <= movedR < n or not 0 <= movedC < n:
            break
        arr[movedR][movedC] = 0
        curR, curC = movedR, movedC

def moveEmpty():
    temp = []
    curR, curC = sharkR, sharkC
    direction = 0
    flag = False
    moveCnt = 1
    while True:
        for _ in range(2):
            for _ in range(moveCnt):
                movedR, movedC = curR + mR[direction], curC + mC[direction]
                if not 0 <= movedR < n or not 0 <= movedC < n:
                    flag = True
                    break
                if arr[movedR][movedC] == 0:
                    curR, curC = movedR, movedC
                    continue


                temp.append(arr[movedR][movedC])



                curR, curC = movedR, movedC
            if flag:
                break
            direction += 1
            direction %= 4
        if flag:
            break
        moveCnt += 1

    newArr = [[0] * n for _ in range(n)]
    curR, curC = sharkR, sharkC
    direction = 0
    flag = False
    moveCnt = 1
    tempIdx = 0
    while True:
        for _ in range(2):
            for _ in range(moveCnt):
                movedR, movedC = curR + mR[direction], curC + mC[direction]
                if not 0 <= movedR < n or not 0 <= movedC < n or len(temp) <= tempIdx:
                    flag = True
                    break


                newArr[movedR][movedC] = temp[tempIdx]
                tempIdx += 1



                curR, curC = movedR, movedC
            if flag:
                break
            direction += 1
            direction %= 4
        if flag:
            break
        moveCnt += 1

    return newArr


def 폭발():
    global explosion
    curR, curC = sharkR, sharkC
    direction = 0
    flag = False
    moveCnt = 1
    temp = []
    curNum = 0
    isExplode = False
    while True:
        for _ in range(2):
            for _ in range(moveCnt):
                movedR, movedC = curR + mR[direction], curC + mC[direction]
                if not 0 <= movedR < n or not 0 <= movedC < n or arr[movedR][movedC] == 0:
                    flag = True
                    break

                # 그루핑
                if curNum != arr[movedR][movedC]:
                    if 4 <= len(temp):
                        isExplode = True
                        for explodeR, explodeC in temp:
                            arr[explodeR][explodeC] = 0
                            explosion[curNum - 1] += 1
                    curNum = arr[movedR][movedC]
                    temp = [[movedR, movedC]]
                else:
                    temp.append([movedR, movedC])



                curR, curC = movedR, movedC
            if flag:
                break
            direction += 1
            direction %= 4
        if flag:
            break
        moveCnt += 1

    # 후처리
    if 4 <= len(temp) and curNum != 0:
        isExplode = True
        for explodeR, explodeC in temp:
            arr[explodeR][explodeC] = 0
            explosion[curNum - 1] += 1

    return isExplode

def 연속구슬():
    # [개수, 번호] 만들기
    temp = []
    curR, curC = sharkR, sharkC
    direction = 0
    flag = False
    moveCnt = 1

    cnt = 0
    curNum = 0
    while True:
        for _ in range(2):
            for _ in range(moveCnt):
                movedR, movedC = curR + mR[direction], curC + mC[direction]
                if not 0 <= movedR < n or not 0 <= movedC < n or arr[movedR][movedC] == 0:
                    flag = True
                    break
                    

                if arr[movedR][movedC] != curNum:
                    temp.append([cnt, curNum])
                    cnt = 1
                    curNum = arr[movedR][movedC]
                else:
                    cnt += 1

                curR, curC = movedR, movedC
            if flag:
                break
            direction += 1
            direction %= 4
        if flag:
            break
        moveCnt += 1

    if curNum != 0:
        temp.append([cnt, curNum])

    # 2개씩 넣기
    if temp:
        temp.pop(0)
    tempList = []
    for numOf, num in temp:
        tempList.append(numOf)
        tempList.append(num)
    newArr = [[0] * n for _ in range(n)]
    curR, curC = sharkR, sharkC
    direction = 0
    flag = False
    moveCnt = 1
    idx = 0
    while True:
        for _ in range(2):
            for _ in range(moveCnt):
                movedR, movedC = curR + mR[direction], curC + mC[direction]
                if not 0 <= movedR < n or not 0 <= movedC < n or len(tempList) <= idx:
                    flag = True
                    break

                newArr[movedR][movedC] = tempList[idx]
                idx += 1

                curR, curC = movedR, movedC
            if flag:
                break
            direction += 1
            direction %= 4
        if flag:
            break
        moveCnt += 1


    return newArr

explosion = [0, 0, 0]
for d, s in magics:
    파괴()
    arr = moveEmpty()
    while 폭발():
        arr = moveEmpty()
        continue
    arr = 연속구슬()

print(explosion[0] * 1 + explosion[1] * 2 + explosion[2] * 3)