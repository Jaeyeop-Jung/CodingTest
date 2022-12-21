from itertools import combinations
from collections import deque

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

n, m = map(int, input().split())
arr = []
empty = []
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(len(temp)):
        if temp[c] == 0:
            empty.append([r, c])
    arr.append(temp)

def getEmpty():
    q = deque()
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == 2:
                q.append([r, c])
    tempArr = [i[:] for i in arr]
    while q:
        r, c, = q.popleft()
        for i in range(4):
            movedR = dRow[i] + r
            movedC = dColumn[i] + c
            if not 0 <= movedR < n or not 0 <= movedC < m:
                continue
            if tempArr[movedR][movedC] == 0:
                tempArr[movedR][movedC] = 2
                q.append([movedR, movedC])
    return sum([i.count(0) for i in tempArr])


result = 0
for case in combinations(empty, 3):
    for r, c in case:
        arr[r][c] = 1
    result = max(result, getEmpty())
    for r, c in case:
        arr[r][c] = 0

print(result)