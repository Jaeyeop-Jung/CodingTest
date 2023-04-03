# TODO 틀림

from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def gravity():
    newArr = [i[:] for i in arr]
    for c in range(n):
        stack = []
        for r in range(n):
            if arr[r][c] == -1:
                cnt = 1
                while stack:
                    num = stack.pop()
                    if num == -2:
                        continue
                    else:
                        newArr[r - cnt][c] = num
                        cnt += 1
            else:
                stack.append(arr[r][c])
                newArr[r][c] = -2
        cnt = 0
        while stack:
            num = stack.pop()
            if num == -2:
                continue
            newArr[n - 1 - cnt][c] = num
            cnt += 1
    return newArr

def rotate():
    newArr = [i[:] for i in arr]
    row = 0
    for c in range(n - 1, -1, -1):
        temp = deque()
        for r in range(n):
            temp.append(arr[r][c])
        for newC in range(n):
            newArr[row][newC] = temp[newC]
        row += 1
    return newArr

def findStd(group):
    curR, curC = n, n
    for r, c in group:
        if 1 <= arr[r][c] and [r, c] < [curR, curC]:
            curR, curC = r, c
    return curR, curC


result = 0
while True:
    rainbowCnt = -1
    group = []
    for r in range(n - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            if 1 <= arr[r][c]:
                generalBlock = arr[r][c]
                q = deque()
                q.append([r, c])
                visited = [[False] * n for _ in range(n)]
                visited[r][c] = True
                tempGroup = [[r, c]]
                tempRainbowCnt = 0
                while q:
                    curR, curC, = q.popleft()
                    for d in range(4):
                        movedR, movedC = curR + dR[d], curC + dC[d]
                        if not 0 <= movedR < n or not 0 <= movedC < n or visited[movedR][movedC] or arr[movedR][movedC] == -2:
                            continue
                        if arr[movedR][movedC] == -1 or (1 <= arr[movedR][movedC] and arr[movedR][movedC] != generalBlock):
                            continue
                        if arr[movedR][movedC] == 0:
                            tempRainbowCnt += 1
                        q.append([movedR, movedC])
                        tempGroup.append([movedR, movedC])
                        visited[movedR][movedC] = True
                if 2 <= len(tempGroup):
                    groupR, groupC = findStd(group)
                    tempGroupR, tempGroupC = findStd(tempGroup)
                    if not group:
                        rainbowCnt = tempRainbowCnt
                        group = tempGroup
                    elif len(group) < len(tempGroup):
                        rainbowCnt = tempRainbowCnt
                        group = tempGroup
                    elif len(group) == len(tempGroup) and rainbowCnt < tempRainbowCnt:
                        rainbowCnt = tempRainbowCnt
                        group = tempGroup
                    elif len(group) == len(tempGroup) and rainbowCnt == tempRainbowCnt and [groupR, groupC] < [tempGroupR, tempGroupC]:
                        rainbowCnt = tempRainbowCnt
                        group = tempGroup

    if rainbowCnt == -1 or len(group) < 2:
        break
    result += len(group) ** 2
    for r, c in group:
        arr[r][c] = -2

    arr = gravity()
    arr = rotate()
    arr = gravity()

print(result)