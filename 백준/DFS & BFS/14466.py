import sys
from collections import deque
input = sys.stdin.readline

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

n, k, r, = map(int, input().split())

# 각 칸에서 동남서북에 길이 있는지 나타낼 리스트 정의
board = [[[False] * 4 for _ in range(n)] for _ in range(n)]
for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1 -1, c1 -1, r2 - 1, c2 -1
    for i in range(4):
        movedR, movedC = r1 + dR[i], c1 + dC[i]
        if not 0 <= movedR < n or not 0 <= movedC < n:
            continue
        if r2 == movedR and c2 == movedC:
            board[r1][c1][i] = True
            board[r2][c2][(i + 2) % 4] = True
            break

# 소 위치 저장
cow = []
for _ in range(k):
    r, c = map(int, input().split())
    cow.append([r - 1, c - 1])

result = 0
# 모든 소를 탐색하면서
for i in range(len(cow)):
    q = deque()
    q.append(cow[i])
    visited = [[False] * n for _ in range(n)]
    visited[cow[i][0]][cow[i][1]] = True
    while q:
        curR, curC, = q.popleft()
        for j in range(4):
            movedR, movedC = curR + dR[j], curC + dC[j]
            # 범위를 벗어나면
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            # 이미 방문했다면
            if visited[movedR][movedC]:
                continue
            # 움직이려는 방향이 길이라면
            if board[curR][curC][j]:
                continue
            # 모든 조건에서 걸러지지 않는다면 방문 처리
            visited[movedR][movedC] = True
            q.append([movedR, movedC])

    # BFS를 통해 접근 가능한 곳에 방문 처리를 다 한 뒤에
    for j in range(len(cow)):
        if i == j:
            continue
        # 방문이 안된 소는 쌍을 더해줌
        if not visited[cow[j][0]][cow[j][1]]:
            result += 1

# (1, 3), (3, 1) 이렇게 쌍이 중복되기 때문에 마지막에 나누기 2
print(result // 2)