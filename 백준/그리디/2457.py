# TODO 틀림 어렵지만 잘 생각해봐라

from collections import deque

n = int(input())
arr = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    arr.append([a * 100 + b, c * 100 + d])

arr.sort()
arr = deque(arr)

right = 301
cnt = 0
while arr:
    next = right
    while arr and arr[0][0] <= right:
        next = max(next, arr.popleft()[1])

    if next == right:
        break

    right = next
    cnt += 1
    if 1201 <= right:
        break

print(cnt if 1201 <= right else 0)
