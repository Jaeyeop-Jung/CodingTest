
dR = [0, 1, 1, 0, -1, -1, -1, 0, 1]
dC = [-5, 0, -1, -1, -1, 0, 1, 1, 1]

n = int(input())
priority = [list(map(int, input().split())) for _ in range(8)]
blocks = [list(map(int, input().split())) for _ in range(n)]

arr = [[[] for _ in range(4)] for _ in range(n)]
result = 0

def makeNewArr(arr):
    n = len(arr)
    newArr = [[[] for _ in range(4)] for _ in range(n)]
    for r in range(len(arr)):
        for c in range(4):
            if arr[r][c]:
                newArr[r][c].append(arr[r][c][0])
    return newArr


def gravity(arr):
    n = len(arr)
    newArr = [[[] for _ in range(4)] for _ in range(n)]
    for c in range(4):
        temp = []
        for r in range(n):
            if arr[r][c]:
                temp.append(arr[r][c][0])
        for r in range(len(temp)):
            newArr[r][c].append(temp[r])
    return newArr

def move(arr):
    n = len(arr)
    newArr = [[[] for _ in range(4)] for _ in range(n)]

    # 이동
    for r in range(n):
        for c in range(4):
            if arr[r][c]:
                for i in priority[arr[r][c][0] - 1]:
                    movedR, movedC = r + dR[i], c + dC[i]
                    if movedR < 0 or not 0 <= movedC < 4:
                        continue
                    if n <= movedR:
                        newArr.append([[], [], [], []])
                        n += 1
                    newArr[movedR][movedC].append(arr[r][c][0])
                    break

    # 2개 이상
    for r in range(n):
        for c in range(4):
            if 2 <= len(newArr[r][c]):
                minimum = min(newArr[r][c])
                newArr[r][c] = [minimum]
    return newArr


def getScore(arr):
    n = len(arr)
    newArr = makeNewArr(arr)
    score = 0
    for r in range(n):
        for c in range(4):
            if not arr[r][c]:
                break
        else:
            for c in range(4):
                newArr[r][c] = []
            score += 1

    return score, newArr


def dfs(arr, blocks, idx, score):
    if idx == len(blocks):
        global result
        result = max(result, score)
        return

    blockNum, c = blocks[idx]
    newArr = makeNewArr(arr)
    if c == 0:
        for c in range(4):
            newArr = makeNewArr(arr)
            if newArr[-1][c]:
                newArr.append([[], [], [], []])
            newArr[-1][c].append(blockNum)
            newArr = gravity(newArr)
            tempScore1, newArr = getScore(newArr)
            newArr = gravity(newArr)
            newArr = move(newArr)
            newArr = gravity(newArr)
            tempScore2, newArr = getScore(newArr)
            dfs(newArr, blocks, idx + 1, score + tempScore1 + tempScore2)
    else:
        c -= 1
        newArr[-1][c].append(blockNum)
        newArr = gravity(newArr)
        tempScore1, newArr = getScore(newArr)
        newArr = gravity(newArr)
        newArr = move(newArr)
        newArr = gravity(newArr)
        tempScore2, newArr = getScore(newArr)
        newArr = gravity(newArr)
        dfs(newArr, blocks, idx + 1, score + tempScore1 + tempScore2)


dfs(arr, blocks, 0, 0)
print(result)