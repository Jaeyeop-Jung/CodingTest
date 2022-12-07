
n, m, k = map(int, input().split())

for i in range(k):
    if n // 2 < m:
        m -= 1
    else:
        n -= 1

print(min(n // 2, m))