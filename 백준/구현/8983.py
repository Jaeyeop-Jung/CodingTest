import sys
import heapq

input = sys.stdin.readline

n, m, l, = map(int, input().split())
arr = sorted(list(map(int, input().split())))
targets = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[0])
targets = [target for target in targets if target[1] <= l]

idx = 0
res = 0
m = len(targets)
# 앞
while idx < m and 0 <= targets[idx][0] <= arr[0]:
    if abs(targets[idx][0] - arr[0]) + targets[idx][1] <= l:
        res += 1
    idx += 1

# 가운데
for i in range(len(arr) - 1):
    while idx < m and arr[i] <= targets[idx][0] <= arr[i + 1]:
        if abs(targets[idx][0] - arr[i]) + targets[idx][1] <= l or abs(targets[idx][0] - arr[i + 1]) + targets[idx][1] <= l:
            res += 1
        idx += 1

# 뒤
while idx < m and arr[-1] <= targets[idx][0] <= arr[-1] + l:
    if abs(targets[idx][0] - arr[-1]) + targets[idx][1] <= l:
        res += 1
    idx += 1

print(res)