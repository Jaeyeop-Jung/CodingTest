# 1. d방향 s칸 만큼 구름 이동
# 2. 구름이 있는 칸에 물의 양 1증가
# 3. 대각선 4방향에 0이상 물이 있으면 갯수만큼 증가
# 4. 물이 2이상이면 거기에 구름 생기고, 물 2줄어듬. 전에 구름인 곳은 안됌

from collections import defaultdict

dR = [0, -1, -1, -1, 0, 1, 1, 1]
dC = [-1, -1, 0, 1, 1, 1, 0, -1]

diagonalR = [1, 1, -1, -1]
diagonalC = [1, -1, -1, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
command = [list(map(int, input().split())) for _ in range(m)]

cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

def move():
    for i, v in enumerate(cloud):
        r, c, = v
        movedR, movedC = r + dR[d - 1] * s, c + dC[d - 1] * s
        movedR %= n
        movedC %= n
        cloud[i] = [movedR, movedC]


for d, s in command:
    # 1
    move()

    # 2
    for r, c in cloud:
        arr[r][c] += 1

    # 3
    dic = {i: defaultdict(int) for i in range(n)}
    for r, c in cloud:
        cnt = 0
        for i in range(4):
            movedR, movedC, = r + diagonalR[i], c + diagonalC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if 0 < arr[movedR][movedC]:
                cnt += 1
        arr[r][c] += cnt
        dic[r][c] = 1

    # 4
    newCloud = []
    for r in range(n):
        for c in range(n):
            if 2 <= arr[r][c] and dic[r][c] == 0:
                newCloud.append([r, c])
                arr[r][c] -= 2
    cloud = newCloud

print(sum(map(sum, arr)))