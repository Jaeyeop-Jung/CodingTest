# TODO 틀림

#   1. 몬스터 알 낳음. 방향은 같은 방향
#   2. 몬스터가 방향 대로 이동함.
#       몬스터 시체 or 팩맨 or 격자 밖이면 반시계 방향 45도로 돌림.
#       만약 갈 곳이 없으면 이동하지 않음
#   3. 팩맨은 총 3칸을 이동하는데 상하좌우 우선순위를 갖고 이동함
#   4. 몬스터 시체 소멸(2턴 동안 살아 있음)
#   5. 몬스터 알 부화

dR = [-1, -1, 0, 1, 1, 1, 0, -1]
dC = [0, -1, -1, -1, 0, 1, 1, 1]
pR = [-1, 0, 1, 0]
pC = [0, -1, 0, 1]

m, t, = map(int, input().split())
arr = [[[] for _ in range(4)] for _ in range(4)]
pacmanR, pacmanC = map(int, input().split())
pacmanR -= 1
pacmanC -= 1
for _ in range(m):
    r, c, d = map(int, input().split())
    arr[r - 1][c - 1].append(d - 1)
deadArr = [[[] for _ in range(4)] for _ in range(4)]
eggArr = [[[] for _ in range(4)] for _ in range(4)]

def makeNewArr():
    newArr = [[[] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for num in arr[r][c]:
                newArr[r][c].append(num)
    return newArr

def notInRange(r, c):
    if not 0 <= r < 4 or not 0 <= c < 4:
        return True
    return False

def copyEgg():
    for r in range(4):
        for c in range(4):
            for d in arr[r][c]:
                eggArr[r][c].append(d)

def monsterMove():
    newArr = makeNewArr()
    for r in range(4):
        for c in range(4):
            for num in range(len(arr[r][c]) - 1, -1, -1):
                d = arr[r][c][num]
                for dCnt in range(8):
                    newD = (d + dCnt) % 8
                    movedR, movedC = r + dR[newD], c + dC[newD]
                    if notInRange(movedR, movedC) or deadArr[movedR][movedC] or (movedR == pacmanR and movedC == pacmanC):
                        continue
                    newArr[r][c].pop(num)
                    newArr[movedR][movedC].append(newD)
                    break
    return newArr

def pacmanMove(arr, r, c, totalEat, totalPath):
    if len(totalPath) == 3:
        global eat, path
        if path == [] or len(eat) < len(set(totalEat)):
            eat = list(set(totalEat))
            path = totalPath[:]
        return
    for i in range(4):
        movedR, movedC = r + pR[i], c + pC[i]
        if notInRange(movedR, movedC):
            continue
        for idx in range(len(arr[movedR][movedC])):
            totalEat.append((movedR, movedC, idx))
        totalPath.append(i)
        pacmanMove(arr, movedR, movedC, totalEat, totalPath)
        totalPath.pop()
        for idx in range(len(arr[movedR][movedC])):
            totalEat.pop()

def pacmanEat():
    global pacmanR, pacmanC
    for r, c, idx in eat:
        deadArr[r][c].append(3)
    for r, c, _ in eat:
        arr[r][c] = []
    for i in path:
        pacmanR, pacmanC = pacmanR + pR[i], pacmanC + pC[i]

def deadMonster():
    for r in range(4):
        for c in range(4):
            for i in range(len(deadArr[r][c]) - 1, -1, -1):
                deadArr[r][c][i] -= 1
                if deadArr[r][c][i] == 0:
                    deadArr[r][c].pop(i)

def hatchEgg():
    for r in range(4):
        for c in range(4):
            for d in eggArr[r][c]:
                arr[r][c].append(d)
    return [[[] for _ in range(4)] for _ in range(4)]

for _ in range(t):

    # 1
    copyEgg()

    # 2
    arr = monsterMove()

    # 3
    eat = []
    path = []
    pacmanMove(arr, pacmanR, pacmanC, [], [])
    pacmanEat()

    # 4
    deadMonster()

    # 5
    eggArr = hatchEgg()

result = 0
for r in range(4):
    for c in range(4):
        result += len(arr[r][c])
print(result)