import sys
from collections import deque

input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, m, = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

visited = [[-1] * m for _ in range(n)]
group = 1
score = {}
for r in range(n):
    for c in range(m):
        if arr[r][c] == 1:
            for d in range(4):
                sR, sC = r + dR[d], c + dC[d]
                if not 0 <= sR < n or not 0 <= sC < m or visited[sR][sC] != -1 or arr[sR][sC] == 1:
                    continue
                cnt = 1
                q = deque()
                q.append((sR, sC))
                visited[sR][sC] = group
                while q:
                    curR, curC, = q.popleft()
                    for i in range(4):
                        movedR, movedC = curR + dR[i], curC + dC[i]
                        if not 0 <= movedR < n or not 0 <= movedC < m:
                            continue
                        if arr[movedR][movedC] == 1 or visited[movedR][movedC] != -1:
                            continue
                        cnt += 1
                        visited[movedR][movedC] = group
                        q.append((movedR, movedC))
                score[group] = cnt
                group += 1

res = [i[:] for i in arr]
for r in range(n):
    for c in range(m):
        if res[r][c] == 1:
            temp = set()
            for d in range(4):
                movedR, movedC = r + dR[d], c + dC[d]
                if not 0 <= movedR < n or not 0 <= movedC < m:
                    continue
                if visited[movedR][movedC] == -1:
                    continue
                temp.add(visited[movedR][movedC])
            res[r][c] += sum([score[i] for i in temp])

for r in range(n):
    for c in range(m):
        print(res[r][c] % 10, end='')
    print()