import math
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

maxValue = [0] * 4
stack = [[] for _ in range(4)]
for num in arr:
    diff = math.inf
    idx = -1
    for i in range(4):
        if stack[i] and stack[i][-1] < num:
            tempDiff = abs(num - stack[i][-1])
            if tempDiff < diff:
                idx = i
                diff = tempDiff

    if idx == -1:
        for i in range(4):
            if not stack[i]:
                stack[i].append(num)
                break
        else:
            print('NO')
            exit()
    else:
        stack[idx].append(num)

print('YES')