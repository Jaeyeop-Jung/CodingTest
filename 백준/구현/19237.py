# TODO 틀림 이게 왜 틀리냐

dR = [0, -1, 1, 0, 0]
dC = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())
arr = []    # 상어가 있는 board
sharks = {} # 살아 있는 상어들
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(len(temp)):
        if temp[c] != 0:
            sharks[temp[c]] = [r, c]
            temp[c] = [temp[c]]
        else:
            temp[c] = []
    arr.append(temp)
direction = list(map(int, input().split())) # [상어 번호] = 상어 방향
sharkPriority = {}  # 상어들의 우선 순위. [상어 번호][현재 방향] = [다음 우선 순위들]
for shark in range(1, m + 1):
    sharkPriority[shark] = {}
    for d in range(1, 5):
        sharkPriority[shark][d] = list(map(int, input().split()))

def move():
    for shark in range(1, m + 1):
        if shark not in sharks:
            continue
        sharkDirection = direction[shark - 1]
        sharkR, sharkC = sharks[shark]
        for d in sharkPriority[shark][sharkDirection]:  # 냄새가 없는 곳 먼저 찾고
            movedR, movedC = sharkR + dR[d], sharkC + dC[d]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if not smellArr[movedR][movedC]:
                direction[shark - 1] = d
                sharks[shark] = [movedR, movedC]
                arr[sharkR][sharkC].remove(shark)
                arr[movedR][movedC].append(shark)
                break
        else:   # 내 냄새인거 있나 찾고
            for d in sharkPriority[shark][sharkDirection]:
                movedR, movedC = sharkR + dR[d], sharkC + dC[d]
                if not 0 <= movedR < n or not 0 <= movedC < n:
                    continue
                if smellArr[movedR][movedC][0] == shark:
                    direction[shark - 1] = d
                    sharks[shark] = [movedR, movedC]
                    arr[sharkR][sharkC].remove(shark)
                    arr[movedR][movedC].append(shark)
                    break

def smell():
    for r in range(n):
        for c in range(n):
            if smellArr[r][c]:
                smellArr[r][c][1] -= 1
            if arr[r][c]:
                smellArr[r][c] = [arr[r][c][0], k]
            if smellArr[r][c] and smellArr[r][c][1] == 0:
                smellArr[r][c] = []

def eat():
    for r in range(n):
        for c in range(n):
            if arr[r][c]:
                liveShark = min(arr[r][c])
                for shark in arr[r][c]:
                    if shark != liveShark:
                        arr[r][c].remove(shark)
                        del sharks[shark]

smellArr = [[[] for _ in range(n)] for _ in range(n)]
second = 0
while True:
    if len(sharks) == 1 or second == 1001:
        break
    second += 1
    smell()
    move()
    eat()

if len(sharks) == 1 and second < 1001:
    print(second)
else:
    print(-1)