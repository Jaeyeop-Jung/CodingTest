from itertools import product
from collections import deque

n = int(input())
origin = [list(map(int, input().split())) for _ in range(n)]

def getMaxSize():
    global res
    for r in range(n):
        for c in range(n):
            res = max(res, arr[r][c])

def rotate(arr):
    newArr = [[0] * n for _ in range(n)]
    for c in range(n):
        q = deque()
        for r in range(n - 1, -1, -1):
            q.append(arr[r][c])
        for rC in range(n):
            newArr[c][rC] = q.popleft()
    return newArr

def gravity(arr):
    newArr = [[0] * n for _ in range(n)]
    for c in range(n):
        q = deque()
        for r in range(n - 1, -1, -1):
            if arr[r][c] != 0:
                q.append(arr[r][c])
        r = n - 1
        while q:
            newArr[r][c] = q.popleft()
            r -= 1
    return newArr

def hit(arr):
    for c in range(n):
        cnt = 0
        cur = -1
        for r in range(n - 1, -1, -1):
            if cur != arr[r][c]:
                cnt = 1
                cur = arr[r][c]
            else:
                cnt += 1
                if cnt == 2:
                    arr[r + 1][c] += arr[r][c]
                    arr[r][c] = 0
                    cur = -1
    arr = gravity(arr)
    return arr

res = 0
for case in product([0, 1, 2, 3], repeat=5):
    arr = [i[:] for i in origin]
    for each in case:
        # 1 돌리기
        for _ in range(each):
            arr = rotate(arr)

        # 2 중력
        arr = gravity(arr)

        # 3 부딪히기
        arr = hit(arr)

        # 4 되돌리기
        for _ in range(4 - each):
            arr = rotate(arr)

    getMaxSize()

print(res)