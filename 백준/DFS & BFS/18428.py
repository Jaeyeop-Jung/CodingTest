
dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n = int(input())
arr = []
teacher = []
for i in range(n):
    temp = list(input().split())
    for j in range(n):
        if temp[j] == 'T':
            teacher.append([i, j])
    arr.append(temp)

def isMiss(arr):
    for r, c in teacher:
        for i in range(4):
            curR, curC = r, c
            while True:
                curR += dR[i]
                curC += dC[i]
                if not 0 <= curR < n or not 0 <= curC < n:
                    break
                if arr[curR][curC] == 'O':
                    break
                if arr[curR][curC] == 'S':
                    return False
    return True


def dfs(arr, cnt):
    if cnt == 3:
        if isMiss(arr):
            print('YES')
            exit()
        return

    for r in range(n):
        for c in range(n):
            if arr[r][c] == 'X':
                arr[r][c] = 'O'
                dfs(arr, cnt + 1)
                arr[r][c] = 'X'

dfs(arr, 0)

print('NO')