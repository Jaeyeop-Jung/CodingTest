import sys

input = sys.stdin.readline

n, m, k, = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

whiteArr = [[0] * m for _ in range(n)]
blackArr = [[0] * m for _ in range(n)]

white = 0
whiteCnt = 0
black = 0
blackCnt = 0
for r in range(n):
    for c in range(m):
        # 화이트
        if whiteCnt % 2 == 0 and arr[r][c] == 'B':
            whiteArr[r][c] += 1
        # 블랙
        elif whiteCnt % 2 == 1 and arr[r][c] == 'W':
            whiteArr[r][c] += 1

        # 블랙
        if blackCnt % 2 == 0 and arr[r][c] == 'W':
            blackArr[r][c] += 1
        # 화이트
        elif blackCnt % 2 == 1 and arr[r][c] == 'B':
            blackArr[r][c] += 1

        whiteCnt = (whiteCnt + 1) % 2
        blackCnt = (blackCnt + 1) % 2
    if m % 2 == 0:
        whiteCnt = (whiteCnt + 1) % 2
        blackCnt = (blackCnt + 1) % 2

def getPrefixSum(arr):
    newArr = [[0] * m for _ in range(n)]
    for r in range(n):
        cnt = 0
        for c in range(m):
            if arr[r][c] == 1:
                cnt += 1
            newArr[r][c] = cnt

    for c in range(m):
        cnt = newArr[0][c]
        for r in range(1, n):
            cnt += newArr[r][c]
            newArr[r][c] = cnt

    return newArr

def getCost(arr, sR, sC, eR, eC):
    temp = arr[eR][eC]
    if sR != 0:
        temp -= arr[sR - 1][eC]
    if sC != 0:
        temp -= arr[eR][sC - 1]
    if 1 <= sR and 1 <= sC:
        temp += arr[sR - 1][sC - 1]
    return temp

whiteArr = getPrefixSum(whiteArr)
blackArr = getPrefixSum(blackArr)

res = sys.maxsize
for r in range(n):
    for c in range(m):
        if r + k - 1 < n and c + k - 1 < m:
            res = min(res, getCost(whiteArr, r, c, r + k - 1, c + k - 1))
            res = min(res, getCost(blackArr, r, c, r + k - 1, c + k - 1))
print(res)