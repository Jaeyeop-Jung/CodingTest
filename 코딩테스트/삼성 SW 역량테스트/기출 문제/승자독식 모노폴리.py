'''
1. 시작할 때 칸을 독점한다
2. 독점은 k 만큼 유지된다
3. 이동 우선 순위에 따라
    - 인접한 독점계약이 없는 칸
    - 내가 독점한 칸
4. 이동 후 2명 이상이 있으면 번호가 가장 작은 사람만 남는다
'''

dR = [-1, 1, 0, 0]
dC = [0, 0, -1, 1]

n, m, k, = map(int, input().split())
player = {}
arr = [[[] for _ in range(n)] for _ in range(n)]
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(n):
        if temp[c] != 0:
            player[temp[c]] = [r, c]
            arr[r][c].append(temp[c])

temp = list(map(int, input().split()))
for num in range(len(temp)):
    player[num + 1].append(temp[num] - 1)
for num in range(m):
    priority = []
    for d in range(4):
        temp = list(map(int, input().split()))
        for c in range(4):
            temp[c] -= 1
        priority.append(temp)
    player[num + 1].append(priority)

def conquer():
    for num in player:
        r, c, d, priority, = player[num]
        if conquerArr[r][c]:
            conquerArr[r][c] = []
        conquerArr[r][c].append([num, k])

def move():
    for num in player:
        r, c, d, priority = player[num]
        flag = False
        # 인접한 독점 계약이 없는 칸 찾기
        for dCnt in range(4):
            curD = (d + dCnt) % 4
            for priorityD in priority[curD]:
                movedR, movedC = r + dR[priorityD], c + dC[priorityD]
                if not 0 <= movedR < n or not 0 <= movedC < n:
                    continue
                if not conquerArr[movedR][movedC]:
                    player[num] = [movedR, movedC, priorityD, priority]
                    arr[movedR][movedC].append(num)
                    arr[r][c].remove(num)
                    flag = True
                    break
            if flag:
                break
        else:   # 내가 독점한 칸으로
            for dCnt in range(4):
                curD = (d + dCnt) % 4
                for priorityD in priority[curD]:
                    movedR, movedC = r + dR[priorityD], c + dC[priorityD]
                    if not 0 <= movedR < n or not 0 <= movedC < n:
                        continue
                    if conquerArr[movedR][movedC] and conquerArr[movedR][movedC][0][0] == num:
                        player[num] = [movedR, movedC, priorityD, priority]
                        arr[movedR][movedC].append(num)
                        arr[r][c].remove(num)
                        flag = True
                        break
                if flag:
                    break

def fight():
    for r in range(n):
        for c in range(n):
            if 2 <= len(arr[r][c]):
                minNum = min(arr[r][c])
                for num in arr[r][c]:
                    if num != minNum:
                        arr[r][c].remove(num)
                        del player[num]

def reduceConquer():
    for r in range(n):
        for c in range(n):
            if conquerArr[r][c]:
                conquerArr[r][c][0][1] -= 1
                if conquerArr[r][c][0][1] == 0:
                    conquerArr[r][c] = []

conquerArr = [[[] for _ in range(n)] for _ in range(n)]
for round in range(1, 1001):
    conquer()
    move()
    fight()
    reduceConquer()
    if len(player) == 1:
        print(round)
        break
else:
    print(-1)