#   4 x 4 격자

#   물고기
#   - M마리가 존재
#   - 8방향 중 하나를 갖고 있다
#   - 상어도 존재한다

#   마법
#   1. 복제 마법은 5번에서 물고기 복제가 나타난다
#   2. 모든 물고기가 한 칸 이동한다
#   - 상어가 있거나 or 물고기의 냄새가 있거나 or 격자의 범위 밖으로는 이동할 수 없다
#   - 이동을 못한다면 45도를 반시계 회전한다
#   - 이동할 칸이 없다면 이동하지 않는다.
#   3. 상어가 가능한 이동 방법 중 가장 많은 물고기를 잡는 방향으로 상하좌우 3칸을 이동한다
#   - 여러가지라면 사전순으로 빠른
#   - 물고기가 있는 칸으로 가면 물고기는 제외되며 냄새를 남긴다
#   4. 두번 전 물고기의 냄새가 격자에서 사라진다
#   5. 복제 마법이 완료되어, 모든 물고기는 1의 위치와 방향을 그대로 갖고 태어난다

from itertools import product

dR = [0, -1, -1, -1, 0, 1, 1, 1]
dC = [-1, -1, 0, 1, 1, 1, 0, -1]
sDR = [-1, 0, 1, 0]
sDC = [0, -1, 0, 1]

m, s = map(int, input().split())
arr = [[[] for _ in range(4)] for _ in range(4)]
smell = [[-1] * 4 for _ in range(4)]
for _ in range(m):
    r, c, d = map(int, input().split())
    arr[r - 1][c - 1].append(d - 1)
sharkR, sharkC = map(int, input().split())
sharkR, sharkC = sharkR - 1, sharkC - 1

def inRange(r, c):
    if not 0 <= r < 4 or not 0 <= c < 4:
        return False
    return True

def inShark(r, c):
    if r == sharkR and c == sharkC:
        return True
    return False

def move():
    newArr = [[[] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for d in arr[r][c]:
                for i in range(8):
                    nD = (d - i) % 8
                    movedR, movedC = r + dR[nD], c + dC[nD]
                    if not inRange(movedR, movedC) or inShark(movedR, movedC) or sec <= smell[movedR][movedC]:
                        continue
                    newArr[movedR][movedC].append(nD)
                    break
                else:
                    newArr[r][c].append(d)
    return newArr


def sharkMove():
    global sharkR, sharkC

    # 방향 구하기
    eat = -1
    direction = ()
    for each in product([i for i in range(4)], repeat=3):
        tempEat = 0
        curR, curC = sharkR, sharkC
        visited = set()
        for d in each:
            movedR, movedC = curR + sDR[d], curC + sDC[d]
            if not inRange(movedR, movedC):
                break
            if (movedR, movedC) not in visited:
                tempEat += len(arr[movedR][movedC])
            visited.add((movedR, movedC))
            curR, curC = movedR, movedC
        else:
            if eat < tempEat:
                eat = tempEat
                direction = each
            elif eat == tempEat:
                direction = min(direction, each)

    for d in direction:
        sharkR, sharkC = sharkR + sDR[d], sharkC + sDC[d]
        if arr[sharkR][sharkC]:
            arr[sharkR][sharkC] = []
            smell[sharkR][sharkC] = sec + 2

for sec in range(s):
    # 1
    copyArr = [i[:] for i in arr]

    # 2
    arr = move()

    # 3
    sharkMove()

    # 4 냄새 사라짐

    # 5 복제
    for r in range(4):
        for c in range(4):
            arr[r][c].extend(copyArr[r][c])

res = 0
for r in range(4):
    for c in range(4):
        res += len(arr[r][c])
print(res)