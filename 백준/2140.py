n = int(input())
arr = [list(input()) for _ in range(n)]

dR = [0, 1, 1, 1, 0, -1, -1, -1]
dC = [1, 1, 0, -1, -1, -1, 0, 1]

res = 0
board = [[0] * n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if arr[r][c] != '#':
            continue

        for i in range(8):
            movedR, movedC = r + dR[i], c + dC[i]
            if not 0 <= movedR < n or not 0 <= movedC < n:
                continue
            if arr[movedR][movedC] == '#':
                continue
            if int(arr[movedR][movedC]) < board[movedR][movedC] + 1:
                break
        else:
            for i in range(8):
                movedR, movedC = r + dR[i], c + dC[i]
                if not 0 <= movedR < n or not 0 <= movedC < n:
                    continue
                board[movedR][movedC] += 1
            res += 1
print(res)