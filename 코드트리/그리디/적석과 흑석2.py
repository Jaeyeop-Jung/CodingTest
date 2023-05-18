# TODO 틀림

from collections import deque
from bisect import bisect_left

n, m = map(int, input().split())
red = [int(input()) for _ in range(n)]
black = [list(map(int, input().split())) for _ in range(m)]

red.sort()
black.sort(key=lambda x: (x[1], -x[0]))

black = deque(black)
result = 0
while black and red:
    start, end, = black.popleft()
    left = bisect_left(red, start)
    if left < len(red) and start <= red[left] <= end:
        red.pop(left)
        result += 1

print(result)