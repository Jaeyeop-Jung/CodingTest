import math
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n = int(input())
arr = []
for r in range(n):
    temp = list(input())
    for c in range(len(temp)):
        if temp[c] == 'S':
            sR, sC = r, c
        elif temp[c] == 'E':
            eR, eC = r, c
        # if temp[c].isnumeric():
        #     temp[c] = int(temp[c])
    arr.append(temp)

def goEnd(arr, curR, curC, eR, eC):
    q = deque()
    q.append([curR, curC, 0])
    dp = [[math.inf] * n for _ in range(n)]
    dp[curR][curC] = 0
    while q:
        r, c, price, = q.popleft()
        for i in range(4):
            movedR, movedC = r + dR[i], c + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if arr[movedR][movedC] == '#' or dp[movedR][movedC] != math.inf:
                continue
            q.append([movedR, movedC, price + 1])
            dp[movedR][movedC] = price + 1
    return dp[eR][eC]


def dfs(arr, eR, eC, curR, curC, path, cost):
    if 3 <= len(path):
        global result
        endCost = goEnd(arr, curR, curC, eR, eC)
        if cost + endCost < result:
            result = min(result, cost + endCost)
            return

    q = deque()
    q.append([curR, curC, 0])
    dp = [[math.inf] * n for _ in range(n)]
    dp[curR][curC] = 0
    while q:
        r, c, price, = q.popleft()
        for i in range(4):
            movedR, movedC = r + dR[i], c + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if arr[movedR][movedC] == '#' or dp[movedR][movedC] != math.inf:
                continue
            q.append([movedR, movedC, price + 1])
            dp[movedR][movedC] = price + 1

    for r in range(n):
        for c in range(n):
            if arr[r][c].isnumeric() and dp[r][c] != math.inf:
                if not path:
                    num = arr[r][c]
                    arr[r][c] = '.'
                    dfs(arr, eR, eC, r, c, path + [int(num)], cost + dp[r][c])
                    arr[r][c] = num
                elif path[-1] < int(arr[r][c]):
                    num = arr[r][c]
                    arr[r][c] = '.'
                    dfs(arr, eR, eC, r, c, path + [int(num)], cost + dp[r][c])
                    arr[r][c] = num

result = math.inf
dfs(arr, eR, eC, sR, sC, [], 0)
if result == math.inf:
    print(-1)
else:
    print(result)
