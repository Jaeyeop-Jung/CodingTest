
def quardZip(visited, arr, r, c, r2, c2, cur):
    if cur == 0:
        return
    temp = arr[r][c]
    flag = False
    for nextR in range(r, r2):
        for nextC in range(c, c2):
            if temp != arr[nextR][nextC]:
                flag = True
                break
        if flag:
            break
    else:
        for nextR in range(r, r2):
            for nextC in range(c, c2):
                visited[nextR][nextC] = True
        global result
        result.append(temp)
        return
    for nextR in range(r, r2, cur // 2):
        for nextC in range(c, c2, cur // 2):
            quardZip(visited, arr, nextR, nextC, nextR + cur // 2, nextC + cur // 2, cur // 2)

result = []
def solution(arr):
    n = len(arr)
    visited = [[False] * n for _ in range(n)]
    quardZip(visited, arr, 0, 0, n, n, n)

    return [result.count(0), result.count(1)]


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))