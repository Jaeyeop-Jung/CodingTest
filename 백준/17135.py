import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, canD, = map(int, input().split())
originArr = [list(map(int, input().split())) for _ in range(n)]

def down(arr):
    newArr = [[0] * m for _ in range(n)]
    for c in range(m):
        temp = deque()
        temp.append(0)
        for r in range(n):
            temp.append(arr[r][c])
        temp.pop()
        newArr[0][c] = 0
        for r in range(n - 1, -1, -1):
            newArr[r][c] = temp.pop()
    return newArr

def search(arr, r, c):
    q = deque()
    visited = set()
    q.append((r, c, 0))
    visited.add((r, c))
    canAttack = []
    while q:
        curR, curC, distance, = q.popleft()
        for d in range(4):
            movedR, movedC = curR + dR[d], curC + dC[d]
            if not 0 <= movedR < n or not 0 <= movedC < m:
                continue
            if (movedR, movedC) in visited or canD <= distance:
                continue
            if arr[movedR][movedC] == 1:
                canAttack.append((distance + 1, movedR, movedC))
            q.append((movedR, movedC, distance + 1))
            visited.add((movedR, movedC))
    if canAttack:
        canAttack.sort(key=lambda x: (x[0], x[2]))
        return canAttack[0]
    else:
        return None

def attack(arr, comb):
    target = set()
    for r, c in comb:
        enemy = search(arr, r, c)
        if enemy != None:
            target.add((enemy[1], enemy[2]))
    for r, c in target:
        arr[r][c] = 0

    return len(target)

res = 0
num = [[n, c] for c in range(m)]
for comb in combinations(num, 3):
    arr = [i[:] for i in originArr]
    temp = 0
    for turn in range(n):
        temp += attack(arr, comb)
        arr = down(arr)
    res = max(res, temp)

print(res)