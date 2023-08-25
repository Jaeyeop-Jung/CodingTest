import sys
from collections import defaultdict

input = sys.stdin.readline

n, d, k, c, = map(int, input().split())
arr = [int(input()) for _ in range(n)]

cur = defaultdict(int)
for i in range(k):
    cur[arr[i]] += 1
left = 0
right = k - 1
res = len(cur.keys()) if c in cur else len(cur.keys()) + 1
while left < n:
    cur[arr[left]] -= 1
    if cur[arr[left]] == 0:
        del cur[arr[left]]
    left += 1
    right = (right + 1) % n
    cur[arr[right]] += 1
    res = max(res, len(cur.keys()) if c in cur else len(cur.keys()) + 1)

print(res)
