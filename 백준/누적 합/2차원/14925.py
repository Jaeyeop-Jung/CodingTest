import sys

input = sys.stdin.readline

n, m, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def getScore(r1, c1, r2, c2):
    res = arr[r2][c2]
    if 0 <= r1 - 1:
        res -= arr[r1 - 1][c2]
    if 0 <= c1 - 1:
        res -= arr[r2][c1 - 1]
    if 0 <= r1 - 1 and 0 <= c1 - 1:
        res += arr[r1 - 1][c1 - 1]
    return res


for r in range(n):
    cur = 0
    for c in range(m):
        cur += arr[r][c]
        arr[r][c] = cur
for c in range(m):
    cur = 0
    for r in range(n):
        cur += arr[r][c]
        arr[r][c] = cur

res = 0
for r in range(n):
    for c in range(m):
        cnt = 0
        while True:
            r2 = r + cnt
            c2 = c + cnt
            if n <= r2 or m <= c2:
                break

            score = getScore(r, c, r2, c2)
            if score == 0:
                res = max(res, cnt + 1)
            else:
                break
            cnt += 1

print(res)
