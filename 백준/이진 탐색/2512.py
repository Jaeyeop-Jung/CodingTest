# TODO 틀림 https://claude-u.tistory.com/447

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start = 0
end = max(arr)
result = 0
while start <= end:
    mid = (end + start) // 2
    total = sum([min(mid, i) for i in arr])
    if total <= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
