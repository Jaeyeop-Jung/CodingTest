import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
index = list(map(int, input().split()))
values = list(map(int, input().split()))
m = int(input())
add = deque(list(map(int, input().split())))

q = deque()
for i in range(n):
    if index[i] == 0:
        q.append(values[i])

res = []
for i in range(m):
    q.appendleft(add[i])
    if q:
        res.append(q.pop())

print(*res)