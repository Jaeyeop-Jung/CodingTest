from collections import deque

dR = [0, 1, 1, 1, 0, -1, -1, -1]
dC = [1, 1, 0, -1, -1, -1, 0, 1]

def solution(grid):
    visited = [[-1] * len(grid[i]) for i in range(len(grid))]
    id = 0
    for r in range(len(visited)):
        for c in range(len(visited[r])):
            if grid[r][c] == '#' and visited[r][c] == -1:
                q = deque()
                q.append([r, c])
                visited[r][c] = id
                while q:
                    curR, curC, = q.popleft()
                    for i in range(len(dR)):
                        movedR, movedC = curR + dR[i], curC + dC[i]
                        if not 0 <= movedR < len(grid) or not 0 <= movedC < len(grid[0]):
                            continue
                        if visited[movedR][movedC] != -1 or grid[movedR][movedC] != '#':
                            continue
                        visited[movedR][movedC] = id
                        q.append([movedR, movedC])
                id += 1

    print(visited)

# print(solution(
# [".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."]))
print(solution([".#.", "#..", ".#."]))



