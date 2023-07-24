import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (-x[1], -x[0]))

q = deque(arr)
cur = sys.maxsize
while q:
    cost, end = q.popleft()
    if end <= cur:
        cur = end - cost
    else:
        cur -= cost

print(cur if 1 <= cur else -1)