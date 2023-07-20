import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
cur = 1
for i in range(n):
    if arr[i] <= cur:
        cur += arr[i]
    else:
        print(cur)
        exit()
print(sum(arr) + 1)
