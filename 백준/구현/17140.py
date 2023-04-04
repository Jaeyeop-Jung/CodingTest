from collections import defaultdict

r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = [list(map(int, input().split())) for _ in range(3)]

def commandR():
    temp = []
    for r in range(len(arr)):
        count = defaultdict(int)
        for c in range(len(arr[r])):
            count[arr[r][c]] += 1
        countList = [[key, count[key]] for key in count if key != 0]
        countList.sort(key=lambda x: (x[1], x[0]))
        tempCountList = []
        for x1, x2 in countList:
            tempCountList.append(x1)
            tempCountList.append(x2)
        temp.append(tempCountList)
    return temp

def commandC():
    temp = [[0] * len(arr[0]) for _ in range(len(arr) * 2)]
    for c in range(len(arr[0])):
        count = defaultdict(int)
        for r in range(len(arr)):
            count[arr[r][c]] += 1
        countList = [[key, count[key]] for key in count if key != 0]
        countList.sort(key=lambda x: (x[1], x[0]))
        tempCountList = []
        for x1, x2 in countList:
            tempCountList.append(x1)
            tempCountList.append(x2)
        for r in range(len(tempCountList)):
            temp[r][c] = tempCountList[r]

    # 행 커트
    for r in range(len(temp) - 1, -1, -1):
        for c in range(len(temp[r])):
            if temp[r][c] != 0:
                break
        else:
            temp = temp[:r + 1]

    # 열 커트
    for c in range(len(temp[0]) - 1, -1, -1):
        for r in range(len(temp)):
            if temp[r][c] != 0:
                break
        else:
            temp = [i[:-1] for i in temp]

    return temp

def full(temp):
    maxColumn = 0
    for r in range(len(temp)):
        maxColumn = max(maxColumn, len(temp[r]))
    for r in range(len(temp)):
        if len(temp[r]) < maxColumn:
            temp[r] += [0] * (maxColumn - len(temp[r]))
    return temp

for second in range(101):
    if r <= len(arr) - 1 and c <= len(arr[0]) - 1 and arr[r][c] == k:
        print(second)
        exit()

    rNum = len(arr)
    cNum = len(arr[0])

    if 100 < rNum:
        arr = [arr[r][:] for r in range(100)]
    if 100 < cNum:
        cnt = cNum - 100
        for r in range(rNum):
            for _ in range(cnt):
                arr[r].pop()

    if rNum >= cNum:
        temp = commandR()
        arr = full(temp)
    else:
        arr = commandC()


print(-1)