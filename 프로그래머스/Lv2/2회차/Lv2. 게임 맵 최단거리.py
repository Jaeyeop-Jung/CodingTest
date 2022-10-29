import math
from collections import deque

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

def solution(maps):
    visited = [[math.inf] * len(maps[i]) for i in range(len(maps))]
    q = deque()
    q.append([0, 0, 1])

    while q:
        r, c, cnt = q.popleft()
        for i in range(len(dRow)):
            movedR, movedC = r + dRow[i], c + dColumn[i]
            if not 0 <= movedR < len(maps) or not 0 <= movedC < len(maps[0]):
                continue
            if cnt + 1 < visited[movedR][movedC] and maps[movedR][movedC] != 0:
                q.append([movedR, movedC, cnt + 1])
                visited[movedR][movedC] = cnt + 1

    if visited[-1][-1] == math.inf:
        return -1
    return visited[-1][-1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))