#   4 x 4 격자

#   물고기
#   - 1 ~ 16까지의 번호가 있음
#   - 각자 8방향 중 하나를 갖고 있음

#   init. 상어가 (0, 0)을 먹고 방향은 (0, 0)의 물고기와 같게 된다
#   1. 물고기가 작은 번호부터 이동한다
#   - 이동 가능한 칸은 빈 칸 or 다른 물고기가 있는 칸
#   - 다른 물고기가 있는 칸으로 가면 그 물고기와 위치를 바꾼다
#   - 이동 불가능한 칸은 상어가 있거나 or 격자 밖
#   - 이동이 불가능하면 45도씩 반시계 방향을 돌린다
#   - 그래도 이동 못하면 이동하지 않는다
#   2-1. 상어가 이동 가능하면
#   - 물고기가 없는 칸 or 격자 밖일 때까지 움직인다
#   - 이동 중에 물고기를 먹지 않는다
#   - 더 이상 못 움직일 때 물고기를 먹는다
#   2-2 못 움직이면 멈춘다

dR = [-1, -1, 0, 1, 1, 1, 0, -1]
dC = [0, -1, -1, -1, 0, 1, 1, 1]

arr = [[[] for _ in range(4)] for _ in range(4)]
for r in range(4):
    temp = list(map(int, input().split()))
    for c in range(0, 8, 2):
        arr[r][c // 2] = [temp[c], temp[c + 1] - 1]

def inRange(r, c):
    if not 0 <= r < 4 or not 0 <= c < 4:
        return False
    return True

def move(arr, sharkR, sharkC):
    for num in range(1, 17):
        flag = False
        for r in range(4):
            for c in range(4):
                if arr[r][c] and arr[r][c][0] == num:
                    num, curD = arr[r][c]
                    for d in range(8):
                        nD = (curD + d) % 8
                        movedR, movedC = r + dR[nD], c + dC[nD]
                        if not inRange(movedR, movedC) or (movedR == sharkR and movedC == sharkC):
                            continue
                        # 빈 칸 or 물고기가 있으면 스왑
                        arr[r][c], arr[movedR][movedC] = arr[movedR][movedC], arr[r][c]
                        arr[movedR][movedC][1] = nD
                        flag = True
                        break
                if flag:
                    break
            if flag:
                break
    return arr

def dfs(arr, sR, sC, sD, total):
    originR, originC = sR, sC
    while True:
        # 1
        newArr = move([[j[:] for j in i] for i in arr], originR, originC)

        # 2
        sR, sC = sR + dR[sD], sC + dC[sD]
        if not inRange(sR, sC):
            global res
            res = max(res, total)
            return
        if not newArr[sR][sC]:
            continue
        nextD = newArr[sR][sC][1]
        nextTotal = total + newArr[sR][sC][0]
        newArr[sR][sC] = []
        dfs(newArr, sR, sC, nextD, nextTotal)


sD = arr[0][0][1]
eat = arr[0][0][0]
arr[0][0] = []
res = 0
dfs(arr, 0, 0, sD, eat)
print(res)
