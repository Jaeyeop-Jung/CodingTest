from collections import deque

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[1])
arr = deque(arr)

result = 0
cur = 0
while arr:
    start, end = arr.popleft()
    if cur <= start:
        cur = end
        result += 1

print(n - result)