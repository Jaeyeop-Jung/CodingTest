#   N x N 격자
#   상어는 1 ~ M의 번호가 주어짐
#   1의 번호를 가진 상어는 가장 강력해서 나머지를 모두 쫓아낼 수 있다

#   init 상어가 자신의 위치에 냄새를 뿌린다
#   1. 1초마다 모든 상어가 동시에 상하좌우 중 하나로 이동하고
#       - 상어가 보고 있는 방향의 우선순위에 따라 냄새가 없는 곳을 찾는다
#       - 만약 그런 곳이 없다면 상어의 냄새가 있는 곳으로 이동한다
#       - 여러 마리의 상어가 있다면 가장 번호가 작은 상어만 남는다
#   2. 냄새를 뿌린다

#   냄새는 상어가 K번 이동하면 사라진다

dR = [-1, 1, 0, 0]
dC = [0, 0, -1, 1]

n, m, k, = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
sharks = {i: [] for i in range(1, m + 1)}
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(n):
        if 0 < temp[c]:
            arr[r][c].append(temp[c])
            sharks[temp[c]].append(r)
            sharks[temp[c]].append(c)
directions = list(map(int, input().split()))
for num in range(1, m + 1):
    sharks[num].append(directions[num - 1] - 1)
priority = {shark: [] for shark in range(1, m + 1)}
for shark in range(1, m + 1):
    for _ in range(4):
        temp = list(map(int, input().split()))
        temp = [i - 1 for i in temp]
        priority[shark].append(temp)
smell = [[[] for _ in range(n)] for _ in range(n)]

def leaveSmell():
    for num in sharks:
        r, c, _, = sharks[num]
        smell[r][c] = [num, k]

def removeSmell():
    for r in range(n):
        for c in range(n):
            if smell[r][c]:
                smell[r][c][1] -= 1
                if smell[r][c][1] <= 0:
                    smell[r][c] = []

def move():
    for num in sharks:
        curR, curC, curD, = sharks[num]
        canMove = -1
        for d in priority[num][curD]:
            movedR, movedC = curR + dR[d], curC + dC[d]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if smell[movedR][movedC]:
                continue
            canMove = d
            break

        # 움직일 곳이 없을 때 우선순위가 높은 나의 냄새 나는 곳 찾기
        if canMove == -1:
            for d in priority[num][curD]:
                movedR, movedC = curR + dR[d], curC + dC[d]
                if not 0 <= movedR < n or not 0 <= movedC < n:
                    continue
                if smell[movedR][movedC][0] != num:
                    continue
                canMove = d
                break

        # 움직인다
        movedR, movedC = curR + dR[canMove], curC + dC[canMove]
        arr[curR][curC].remove(num)
        arr[movedR][movedC].append(num)
        sharks[num] = [movedR, movedC, canMove]

def eat():
    for r in range(n):
        for c in range(n):
            if 2 <= len(arr[r][c]):
                minShark = min(arr[r][c])
                for num in arr[r][c]:
                    if minShark != num:
                        del sharks[num]
                arr[r][c] = [minShark]

flag = False
leaveSmell()
for second in range(1, 1001):
    move()
    eat()
    if len(sharks) == 1:
        flag = True
        break
    removeSmell()
    leaveSmell()

print(second if flag else -1)