import math
import sys
from collections import deque
input = sys.stdin.readline

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

n = int(input())
arr = []
for r in range(n):
    temp = list(map(int, input().split()))
    for c in range(len(temp)):
        if temp[c] == 9:
            cur = [r, c]
            temp[c] = 0
            break
    arr.append(temp)

def findNext(r, c):
    q = deque()
    q.append([r, c, 0])
    visited = [[-1] * n for _ in range(n)]
    visited[r][c] = 0
    result = []
    resultCnt = math.inf
    while q:
        curR, curC, cnt = q.popleft()
        for i in range(4):
            movedR, movedC = curR + dRow[i], curC + dColumn[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if visited[movedR][movedC] != -1:
                continue
            if babySharkSize < arr[movedR][movedC]:
                continue
            if arr[movedR][movedC] != 0 and arr[movedR][movedC] < babySharkSize and cnt + 1 < resultCnt:
                result.append([movedR, movedC, cnt + 1])
            q.append([movedR, movedC, cnt + 1])
            visited[movedR][movedC] = cnt + 1
    if not result:
        return False
    else:
        result.sort(key=lambda x: (x[2], x[0], x[1]))
        return result[0]

babySharkSize = 2
babySharkEat = 0
result = 0
while True:
    next = findNext(cur[0], cur[1])
    if next == False:
        break
    cur = [next[0], next[1]]
    arr[cur[0]][cur[1]] = 0
    result += next[2]
    babySharkEat += 1
    if babySharkEat == babySharkSize:
        babySharkEat = 0
        babySharkSize += 1

print(result)