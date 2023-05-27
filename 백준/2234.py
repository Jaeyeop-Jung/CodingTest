# TODO 틀림 맞긴 했는데 나이브했다. 더 고민해봐

from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def convert(d):
    res = [0, 1, 2, 3]
    if 8 <= d:
        res.remove(1)
        d -= 8
    if 4 <= d:
        res.remove(0)
        d -= 4
    if 2 <= d:
        res.remove(3)
        d -= 2
    if 1 <= d:
        res.remove(2)
        d -= 1
    return res

def getOneAndTwo():
    visited = [[False] * m for _ in range(n)]
    numOfRoom = 0
    maxRoomSize = 0
    for r in range(n):
        for c in range(m):
            if not visited[r][c]:
                numOfRoom += 1
                visited[r][c] = True
                q = deque()
                q.append([r, c])
                tempSize = 1
                while q:
                    curR,curC = q.popleft()
                    d = convert(arr[curR][curC])
                    for i in range(len(d)):
                        movedR, movedC = curR + dR[d[i]], curC + dC[d[i]]
                        if not 0 <= movedR < n or not 0 <= movedC < m:
                            continue
                        if visited[movedR][movedC]:
                            continue
                        visited[movedR][movedC] = True
                        q.append([movedR, movedC])
                        tempSize += 1
                maxRoomSize = max(maxRoomSize, tempSize)
    return numOfRoom,maxRoomSize

def getThree():
    res = 0
    for r in range(n):
        for c in range(m):
            d = convert(arr[r][c])
            al = [0, 1, 2, 3]
            for i in d:
                al.remove(i)
            for i in al:
                if i == 0:
                    arr[r][c] -= 4
                    _, temp = getOneAndTwo()
                    arr[r][c] += 4
                elif i == 1:
                    arr[r][c] -= 8
                    _, temp = getOneAndTwo()
                    arr[r][c] += 8
                elif i == 2:
                    arr[r][c] -= 1
                    _, temp = getOneAndTwo()
                    arr[r][c] += 1
                elif i == 3:
                    arr[r][c] -= 2
                    _, temp = getOneAndTwo()
                    arr[r][c] += 2
                res = max(res, temp)
    return res


one, two = getOneAndTwo()
three = getThree()
print(one)
print(two)
print(three)

