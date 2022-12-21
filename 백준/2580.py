# TODO 틀림

empty = []
arr = []
for r in range(9):
    temp = list(map(int, input().split()))
    for c in range(len(temp)):
        if temp[c] == 0:
            empty.append([r, c])
    arr.append(temp)

def find_garo(r):
    temp = [i for i in range(1, 10)]
    for i in range(9):
        if arr[r][i] != 0:
            temp.remove(arr[r][i])
    if len(temp) == 1:
        return temp[0]
    else:
        return False

def find_sero(c):
    temp = [i for i in range(1, 10)]
    for i in range(9):
        if arr[i][c] != 0:
            temp.remove(arr[i][c])
    if len(temp) == 1:
        return temp[0]
    else:
        return False

def find_3x3(r, c):
    r_idx = r // 3
    c_idx = c // 3
    temp = [i for i in range(1, 10)]
    for curR in range(r_idx * 3, r_idx * 3 + 3):
        for curC in range(c_idx * 3, c_idx * 3 + 3):
            if arr[curR][curC] != 0:
                temp.remove(arr[curR][curC])
    if len(temp) == 1:
        return temp[0]
    else:
        return False

visited = [False] * len(empty)
def dfs(arr):
    if False not in visited:
        for i in arr:
            print(*i)
        exit()

    for i in range(len(empty)):
        if visited[i]:
            continue
        r, c = empty[i]
        if find_sero(r) == False or find_garo(c) == False or find_3x3(r, c) == False:
            continue
        if find_garo(r) == find_sero(c) == find_3x3(r, c):
            arr[r][c] = find_garo(r)
            visited[i] = True
            dfs(arr)
            arr[r][c] = 0
            visited[i] = False

dfs(arr)
