# TODO 틀림

import sys

input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

start = 0
end = max(arr) - min(arr)

result = 0
while start <= end:
    mid = (start + end) // 2
    cur = 0
    count = 1
    for i in range(1, len(arr)):
        if arr[i] - arr[cur] >= mid:
            cur = i
            count += 1

    if count < c:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)