import math

arr = []
check = []
for i in range(10):
    temp = list(map(int, input().split()))
    for j in range(10):
        if temp[j] == 1:
            check.append([i, j])
    arr.append(temp)

availableCnt = [5, 5, 5, 5, 5]
def dfs(arr, visited, check, idx, cnt):
    if idx == len(check):
        global result
        result = min(result, cnt)
        return

    r, c = check[idx]
    if visited[r][c]:
        dfs(arr, visited, check, idx + 1, cnt)
    else:
        # 크기 경우의 수 대입
        available = getAvailable(arr, visited, r, c)
        for i in available:
            if availableCnt[i - 1] <= 0:
                continue
            for curR in range(r, r + i):
                for curC in range(c, c + i):
                    visited[curR][curC] = True
            availableCnt[i - 1] -= 1
            dfs(arr, visited, check, idx + 1, cnt + 1)
            availableCnt[i - 1] += 1
            for curR in range(r, r + i):
                for curC in range(c, c + i):
                    visited[curR][curC] = False


def getAvailable(arr, visited, r, c):
    result = []
    for i in range(1, 6):
        for curR in range(r, r + i):
            for curC in range(c, c + i):
                if not 0 <= curR < 10 or not 0 <= curC < 10:
                    return result
                if arr[curR][curC] == 0 or visited[curR][curC]:
                    return result
        result.append(i)
    return result



result = math.inf
visited = [[False] * 10 for _ in range(10)]
dfs(arr, visited, check, 0, 0)
print(result if result != math.inf else -1)