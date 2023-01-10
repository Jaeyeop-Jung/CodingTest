# TODO 틀림 맞출 수 있다 더 고민해봐

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def getCnt():
    cnt = 0
    total = 0
    for i in range(len(arr)):
        if total + arr[i] <= mid:
            total += arr[i]
        else:
            cnt += arr[i] // mid + 1
            total = arr[i] % mid
    return cnt

start = 0
end = sum(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = getCnt()
    if cnt < m:
        end = mid - 1
    else:
        start = mid + 1

print(max(start, max(arr)))
