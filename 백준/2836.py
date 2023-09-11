# TODO 틀림

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    if end <= start:
        arr.append([start, end])

arr.sort(key=lambda x: (x[1], -x[0]))
end = arr[0][1]
res = 0
visited = [False] * len(arr)
cur = 0
for i in range(len(arr)):
    if visited[i]:
        continue
    visited[i] = True
    res += arr[i][1] - cur
    cur = arr[i][1]
    tempMax = arr[i][0]
    for j in range(i + 1, len(arr)):
        if arr[i][1] <= arr[j][1] <= arr[i][0]:
            visited[j] = True
            tempMax = max(tempMax, arr[j][0])
        else:
            break
    res += (tempMax - cur) * 2

print(res if cur == m else res + (m - cur))