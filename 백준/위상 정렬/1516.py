# TODO 틀림 예외를 잘 찾아라

import math
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
after = {i: set() for i in range(1, n + 1)}
before = {i: set() for i in range(1, n + 1)}
time = {}
degree = [0] * (n + 1)
result = [math.inf] * (n + 1)
q = deque()
for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    for j in range(1, len(temp) - 1):
        after[temp[j]].add(i)
        degree[i] += 1
        before[i].add(temp[j])
    if len(temp) == 2:
        q.append(i)
        result[i] = time[i]

while q:
    pop = q.popleft()
    for next in after[pop]:
        degree[next] -= 1
        if degree[next] == 0:
            result[next] = max([result[key] for key in before[next]]) + time[next]
            q.append(next)

for i in range(1, n + 1):
    print(result[i])
