
dR = [0, 1, 1, 1, 0, -1, -1, -1]
dC = [1, 1, 0, -1, -1, -1, 0, 1]

n, m, k = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]
food = [[5] * n for _ in range(n)]
addFood = [list(map(int, input().split())) for _ in range(n)]
# woods = [list(map(int, input().split())) for _ in range(m)]
# for x, y, z in woods:
#     arr[x][y].append(z)
for _ in range(m):
    x, y, z = map(int, input().split())
    arr[x - 1][y - 1].append(z)

for _ in range(k):
    # 봄
    dead = [[[] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr[r][c].sort()
            deadCnt = 0
            for i in range(len(arr[r][c])):
                if arr[r][c][i] <= food[r][c]:
                    food[r][c] -= arr[r][c][i]
                    arr[r][c][i] += 1
                else:
                    dead[r][c].append(arr[r][c][i])
                    deadCnt += 1
            for _ in range(deadCnt):
                arr[r][c].pop()

    # 여름
    for r in range(n):
        for c in range(n):
            for age in dead[r][c]:
                food[r][c] += int(age / 2)

    # 가을
    for r in range(n):
        for c in range(n):
            for i in range(len(arr[r][c])):
                if arr[r][c][i] != 0 and arr[r][c][i] % 5 == 0:
                    for d in range(8):
                        movedR, movedC = r + dR[d], c + dC[d]
                        if not 0 <= movedR < n or not 0 <= movedC < n:
                            continue
                        arr[movedR][movedC].append(1)

    # 겨울
    for r in range(n):
        for c in range(n):
            food[r][c] += addFood[r][c]

result = sum([len(arr[r][c]) for r in range(n) for c in range(n)])
print(result)