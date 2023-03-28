
dR = [-1, -1, 0, 1, 1, 1, 0, -1]
dC = [0, -1, -1, -1, 0, 1, 1, 1]

arr = [[[] for _ in range(4)] for _ in range(4)]
direction = [0] * 17
for r in range(4):
    temp = list(map(int, input().split()))
    for c in range(0, 8, 2):
        arr[r][c // 2] = temp[c]
        direction[temp[c]] = temp[c + 1] - 1

def find(arr, num):
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == num:
                return r, c

def move(arr, direction):
    newArr = [i[:] for i in arr]
    newDirection = direction[:]
    for num in range(1, 17):
        findRecoord = find(newArr, num)
        if findRecoord == None:
            continue
        r, c = findRecoord
        for rotate in range(8):
            d = newDirection[num]
            d = (d + rotate) % 8
            movedR, movedC = r + dR[d], c + dC[d]
            if not 0 <= movedR < 4 or not 0 <= movedC < 4:
                continue
            if newArr[movedR][movedC] == shark:
                continue
            if newArr[movedR][movedC] == -1:
                newArr[movedR][movedC] = num
                newArr[r][c] = -1
            else:
                changeNum = newArr[movedR][movedC]
                newArr[movedR][movedC] = num
                newArr[r][c] = changeNum
            newDirection[num] = d
            break
    return newArr, newDirection

shark = 0
result = 0
def dfs(arr, direction, total):
    newArr, newDirection = move(arr, direction)
    sharkR, sharkC = find(newArr, shark)
    d = newDirection[shark]
    cnt = 1
    while True:
        movedR, movedC = sharkR, sharkC
        for _ in range(cnt):
            movedR, movedC = movedR + dR[d], movedC + dC[d]
        if not 0 <= movedR < 4 or not 0 <= movedC < 4:
            break
        if newArr[movedR][movedC] == -1:
            cnt += 1
            continue
        eatNum = newArr[movedR][movedC]
        newDirection[shark] = newDirection[eatNum]
        newArr[sharkR][sharkC] = -1
        newArr[movedR][movedC] = shark
        dfs(newArr, newDirection, total + eatNum)
        direction[shark] = d
        newArr, newDirection = move(arr, direction)
        cnt += 1

    global result
    result = max(result, total)

first = arr[0][0]
direction[shark] = direction[first]
arr[0][0] = shark
dfs(arr, direction, first)
print(result)