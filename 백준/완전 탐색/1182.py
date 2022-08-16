from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

if sum(arr) == s:
    cnt += 1
for i in range(1, n):
    for j in combinations(arr, i):
        if sum(j) == s:
            cnt += 1

print(cnt)
