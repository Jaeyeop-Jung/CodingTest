import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

res = 0

# 앞
prefix = [0] * n
for i in range(1, n):
    prefix[i] += prefix[i - 1] + arr[i]
for i in range(1, n):
    res = max(res, prefix[-1] - arr[i] + prefix[-1] - prefix[i])

# 뒤
arr.reverse()
prefix = [0] * n
for i in range(1, n):
    prefix[i] += prefix[i - 1] + arr[i]
for i in range(1, n):
    res = max(res, prefix[-1] - arr[i] + prefix[-1] - prefix[i])

# 가운데
sum1 = sum(arr)
for i in range(1, n - 1):
    res = max(res, sum1 - arr[0] - arr[-1] + arr[i])

print(res)