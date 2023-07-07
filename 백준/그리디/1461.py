from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
arr = deque(arr)
res = 0
if abs(min(arr)) <= abs(max(arr)):
    res += max(arr)
    for _ in range(m):
        if arr and 0 < arr[-1]:
            arr.pop()
else:
    res += abs(min(arr))
    for _ in range(m):
        if arr and arr[0] < 0:
            arr.popleft()

# 양수
while arr and 0 < arr[-1]:
    res += arr[-1] * 2
    for _ in range(m):
        if arr and 0 < arr[-1]:
            arr.pop()

# 음수
while arr and arr[0] < 0:
    res += abs(arr[0]) * 2
    for _ in range(m):
        if arr:
            arr.popleft()

print(res)