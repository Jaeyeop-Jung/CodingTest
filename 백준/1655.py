# TODO 틀림 잘 생각해봐라

import sys

input = sys.stdin.readline

n = int(input())
left = []
right = []
left.append(-int(input()))
for _ in range(n - 1):
    inp = int(input())
    heapq.heappush(left, inp)

