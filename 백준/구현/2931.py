# import sys
#
# input = sys.stdin.readline
#
# dR = [0, 1, 0, -1]
# dC = [1, 0, -1, 0]
#
# tunnel = {
#     '|': [1, 3],
#     '-': [0, 2],
#     '+': [0, 1, 2, 3],
#     '1': {2: 1, 3: 0},
#     '2': {1: 0, 2: 3},
#     '3': {1: 2, 0: 3},
#     '4': {0: 1, 3: 2}
# }
#
# n, m = map(int, input().split())
# totalGas = 0
# arr = []
# for _ in range(n):
#     temp = list(input().strip())
#     for i in range(m):
#         if temp[i] != '.' and temp[i] != 'M' and temp[i] != 'Z':
#             if temp[i] == '+':
#                 totalGas += 2
#             else:
#                 totalGas += 1
#         if temp[i] == 'M':
#             sR, sC = _, i
#         if temp[i] == 'Z':
#             tR, tC = _, i
#     arr.append(temp)
#
# def inRange(r, c):
#     if not 0 <= r < n or not 0 <= c < m:
#         return False
#     return True
#
# def isPossible(curD, gas):
#     if curD in tunnel[gas]:
#         return True
#     return False
#
# def getNext(curD, gas):
#     if gas == '|' or gas == '-' or gas == '+':
#         return curD
#     else:
#         return tunnel[gas][curD]
#
# def getNextTunnel(curD):
#     res = []
#     for key in tunnel:
#         if curD in tunnel[key]:
#             res.append(key)
#     return res
#
# def dfs(arr, r, c, d, cnt, added):
#     if arr[r][c] == 'Z':
#         if len(added) == 1 and cnt == totalGas:
#             print(*added[0])
#             exit()
#         return
#
#     movedR, movedC, = r + dR[d], c + dC[d]
#     if inRange(movedR, movedC):
#         if arr[movedR][movedC] == 'Z':
#             dfs(arr, movedR, movedC, d, cnt, added)
#         elif arr[movedR][movedC] == '.':
#             if 1 <= len(added):
#                 return
#             tunnels = getNextTunnel(d)
#             for install in tunnels:
#                 added.append([movedR + 1, movedC + 1, install])
#                 dfs(arr, movedR, movedC, getNext(d, install), cnt, added)
#                 added.pop()
#         else:
#             if isPossible(d, arr[movedR][movedC]):
#                 dfs(arr, movedR, movedC, getNext(d, arr[movedR][movedC]), cnt + 1, added)
#
# for i in range(4):
#     movedR, movedC = sR + dR[i], sC + dC[i]
#     if inRange(movedR, movedC):
#         if arr[movedR][movedC] == '.':
#             tunnels = getNextTunnel(i)
#             for install in tunnels:
#                 dfs(arr, movedR, movedC, getNext(i, install), 1, [movedR + 1, movedC + 1, install])
#         elif isPossible(i, arr[movedR][movedC]):
#             dfs(arr, movedR, movedC, getNext(i, arr[movedR][movedC]), 1, [])

import sys

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

tunnel = {
    '|': [1, 3],
    '-': [0, 2],
    '+': [0, 1, 2, 3],
    '1': {2: 1, 3: 0},
    '2': {1: 0, 2: 3},
    '3': {1: 2, 0: 3},
    '4': {0: 1, 3: 2}
}

n, m = map(int, input().split())
totalGas = 0
arr = []
for _ in range(n):
    temp = list(input().strip())
    for i in range(m):
        if temp[i] != '.' and temp[i] != 'M' and temp[i] != 'Z':
            if temp[i] == '+':
                totalGas += 2
            else:
                totalGas += 1
        if temp[i] == 'M':
            sR, sC = _, i
        if temp[i] == 'Z':
            tR, tC = _, i
    arr.append(temp)

def inRange(r, c):
    if not 0 <= r < n or not 0 <= c < m:
        return False
    return True

def isPossible(curD, gas):
    if curD in tunnel[gas]:
        return True
    return False

def getNext(curD, gas):
    if gas == '|' or gas == '-' or gas == '+':
        return curD
    else:
        return tunnel[gas][curD]

def getNextTunnel(curD):
    res = []
    for key in tunnel:
        if curD in tunnel[key]:
            res.append(key)
    return res

def dfs(arr, r, c, d, cnt, added):
    if arr[r][c] == 'Z':
        if added[0][-1] == '+' and cnt == totalGas + 1:
            print(*added[0])
            exit()
        elif added[0][-1] != '+' and cnt == totalGas:
            print(*added[0])
            exit()
        return

    movedR, movedC, = r + dR[d], c + dC[d]
    if inRange(movedR, movedC):
        if arr[movedR][movedC] == 'Z':
            dfs(arr, movedR, movedC, d, cnt, added)
        elif arr[movedR][movedC] == '.':
            if 1 <= len(added):
                return
            tunnels = getNextTunnel(d)
            for install in tunnels:
                added.append([movedR + 1, movedC + 1, install])
                arr[movedR][movedC] = install
                dfs(arr, movedR, movedC, getNext(d, install), cnt, added)
                arr[movedR][movedC] = '.'
                added.pop()
        else:
            if isPossible(d, arr[movedR][movedC]):
                dfs(arr, movedR, movedC, getNext(d, arr[movedR][movedC]), cnt + 1, added)

for i in range(4):
    movedR, movedC = sR + dR[i], sC + dC[i]
    if inRange(movedR, movedC) and arr[movedR][movedC] != '.' and isPossible(i, arr[movedR][movedC]):
        dfs(arr, movedR, movedC, getNext(i, arr[movedR][movedC]), 1, [])
