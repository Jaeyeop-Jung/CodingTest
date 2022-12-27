from collections import deque
import sys
input = sys.stdin.readline

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

n, left, right, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
while True:
    visited = [[False] * len(arr[0]) for _ in range(len(arr))]
    flag = False
    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if not visited[r][c]:
                q = deque()
                q.append([r, c])
                visited[r][c] = True
                numOfNat = 1
                totalScore = arr[r][c]
                route = [[r, c]]
                while q:
                    curR, curC, = q.popleft()
                    for i in range(4):
                        movedR = curR + dRow[i]
                        movedC = curC + dColumn[i]
                        if not 0 <= movedR < len(arr) or not 0 <= movedC < len(arr[0]):
                            continue
                        if visited[movedR][movedC]:
                            continue
                        if not left <= abs(arr[curR][curC] - arr[movedR][movedC]) <= right:
                            continue
                        q.append([movedR, movedC])
                        route.append([movedR, movedC])
                        visited[movedR][movedC] = True
                        numOfNat += 1
                        totalScore += arr[movedR][movedC]
                if 1 < len(route):
                    score = totalScore // numOfNat
                    for preR, preC in route:
                        arr[preR][preC] = score
                    flag = True

    if flag:
        result += 1
    else:
        break

print(result)
