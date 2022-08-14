# TODO 틀림

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

start = 0
end = max(arr)
result = 0
while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        result = end
        break
    total = sum([i // mid for i in arr])
    if total == k:
        result = mid
    if total < k:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)