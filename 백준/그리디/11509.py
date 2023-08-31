from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

cur = defaultdict(int)
res = 0
for i in range(n):
    if 1 <= cur[arr[i]]:
        cur[arr[i]] -= 1
        cur[arr[i] - 1] += 1
    else:
        cur[arr[i] - 1] += 1
        res += 1

print(res)
