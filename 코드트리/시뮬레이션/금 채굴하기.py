# TODO 틀림

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

total = 0
for r in range(n):
    for c in range(n):
        if arr[r][c] == 1:
            total += 1

def isInRange(r, c):
    if not 0 <= r < n or not 0 <= c < n:
        return False
    return True

result = 0 if total == 0 else 1
for r in range(n):
    for c in range(n):
        k = 1
        while k * k + (k + 1) * (k + 1) <= total * m:
            temp = sum([arr[i][j] for i in range(n) for j in range(n) if abs(r - i) + abs(c - j) <= k])
            if result < temp and k * k + (k + 1) * (k + 1) <= temp * m:
                result = max(result, temp)
            k += 1

print(result)