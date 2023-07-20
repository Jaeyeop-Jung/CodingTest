import math
import sys

input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[0], -x[1]))
res = 0
start = -math.inf
end = -math.inf
for curStart, curEnd in arr:
    # curStart, curEnd, = arr[i]
    if start <= curStart <= curEnd <= end:
        continue
    elif end <= curStart:
        res += curEnd - curStart
    else:
        res += curEnd - curStart - (end - curStart)
    start = curStart
    end = curEnd

print(res)