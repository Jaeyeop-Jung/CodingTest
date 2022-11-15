import sys

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))

def count(arr, tr, tc, tsr, tsc):
    res = 0
    for r in range(tr, tsr + 1):  # row가 증가하면서 가로 확인
        tempCnt = 0
        tempChar = ''
        for c in range(n):
            if tempChar != arr[r][c]:
                res = max(res, tempCnt)
                tempCnt = 1
                tempChar = arr[r][c]
            else:
                tempCnt += 1
        res = max(res, tempCnt)
    for c in range(tc, tsc + 1):  # column이 증가하면서 세로 확인
        tempCnt = 0
        tempChar = ''
        for r in range(n):
            if tempChar != arr[r][c]:
                res = max(res, tempCnt)
                tempCnt = 1
                tempChar = arr[r][c]
            else:
                tempCnt += 1
        res = max(res, tempCnt)
    return res

def swap(arr):
    temp = arr[r][c]
    arr[r][c] = arr[sr][sc]
    arr[sr][sc] = temp
    return arr

result = 0
for r in range(n):
    for c in range(n):
        for k in range(4):
            sr = r + dRow[k]
            sc = c + dColumn[k]
            if not 0 <= sr < n or not 0 <= sc < n:
                continue
            # if arr[r][c] == arr[sr][sc]:
            #     continue
            tempArr = swap([i[:] for i in arr])
            result = max(result, count(tempArr, r, c, sr, sc))

print(result)