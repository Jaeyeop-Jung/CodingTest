# TODO 틀림

import sys

input = sys.stdin.readline

n, s, = map(int, input().split())
m = int(input())
arr = [int(input()) for _ in range(m)]

target = n - s
if target <= m:
    print(target)
    exit()
left, right = 0, 100_000_001
cnt = m
while left <= right:
    mid = (left + right) // 2
    temp = cnt + sum([mid // i for i in arr])
    if temp <= target:
        left = mid + 1
    else:
        right = mid - 1


curCnt = cnt + sum([(left - 1) // i for i in arr])
if curCnt == target:
    for i in range(len(arr) - 1, -1, -1):
        if (left - 1) % arr[i] == 0:
            print(i + 1)
            exit()
else:
    for i in range(m):
        if left % arr[i] == 0:
            curCnt += 1
            if curCnt == target:
                print(i + 1)