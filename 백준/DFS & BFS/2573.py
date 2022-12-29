# TODO 틀림 잘 생각해봐 풀 수 있다

import sys
from collections import deque
input = sys.stdin.readline

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

n, m, = map(int, input().split())
arr = []
target = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if 0 < temp[j]:
            target.append([i, j])
    arr.append(temp)
unFreezeCnt = [[0] * m for _ in range(n)]
for r, c in target:
    for i in range(4):
        movedR = r + dRow[i]
        movedC = c + dColumn[i]
        if not 0 <= movedR < n or not 0 <= movedC < m:
            continue
        if arr[movedR][movedC] == 0:
            unFreezeCnt[r][c] += 1


def getMass():
    visited = [[False] * m for _ in range(n)]
    result = 0
    for r, c in target:
        if arr[r][c] != 0 and not visited[r][c]:
            q = deque()
            q.append([r, c])
            visited[r][c] = True
            while q:
                curR, curC = q.popleft()
                for i in range(4):
                    movedR = curR + dRow[i]
                    movedC = curC + dColumn[i]
                    if not 0 <= movedR < n or not 0 <= movedC < m:
                        continue
                    if visited[movedR][movedC]:
                        continue
                    if arr[movedR][movedC] <= 0:
                        continue
                    q.append([movedR, movedC])
                    visited[movedR][movedC] = True
            result += 1
    return result

def unFreeze():
    curUnFreeze = []
    flag = False
    for i, v in enumerate(target):
        r, c = v
        if 0 < arr[r][c]:
            flag = True
            arr[r][c] = max(0, arr[r][c] - unFreezeCnt[r][c])
            if arr[r][c] == 0:
                curUnFreeze.append(i)

    while curUnFreeze:
        target.pop(curUnFreeze.pop())
        for r, c in target:
            unFreezeCnt[r][c] = 0
            for i in range(4):
                movedR = r + dRow[i]
                movedC = c + dColumn[i]
                if not 0 <= movedR < n or not 0 <= movedC < m:
                    continue
                if arr[movedR][movedC] == 0:
                    unFreezeCnt[r][c] += 1

    if not flag:
        return False
    return True

cnt = 0
while True:
    if 2 <= getMass():
        print(cnt)
        exit()
    if not unFreeze():
        print(0)
        exit()
    cnt += 1
