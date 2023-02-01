from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def solution(maps):
    result = []
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    for r in range(len(maps)):
        for c in range(len(maps[r])):
            if maps[r][c] == 'X' or visited[r][c]:
                continue
            q = deque()
            q.append([r, c])
            temp = int(maps[r][c])
            visited[r][c] = True
            while q:
                curR, curC, = q.popleft()
                for i in range(len(dR)):
                    movedR, movedC = curR + dR[i], curC + dC[i]
                    if not 0 <= movedR < len(maps) or not 0 <= movedC < len(maps[0]):
                        continue
                    if maps[movedR][movedC] == 'X' or visited[movedR][movedC]:
                        continue
                    visited[movedR][movedC] = True
                    q.append([movedR, movedC])
                    temp += int(maps[movedR][movedC])
            result.append(temp)
    if not result:
        return [-1]
    return sorted(result)

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))