import sys
from collections import deque

input = sys.stdin.readline

d, n, = map(int, input().split())
arr = list(map(int, input().split()))
pizza = deque(list(map(int, input().split())))

arr = [[arr[i], i + 1] for i in range(len(arr))]
arr.sort(key=lambda x: (x[0], -x[1]))
arr = deque(arr)

res = []
while pizza:
    pop = pizza.popleft()
    if not res:
        depth = d + 1
    else:
        depth = res[-1]

    while arr and arr[0][0] < pop:
        depth = min(depth, arr.popleft()[1])

    res.append(depth - 1)

print(res[-1] if 0 < res[-1] else 0)
