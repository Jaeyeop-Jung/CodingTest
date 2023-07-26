import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

two = {}
arr.sort()
for i in range(n):
    for j in range(i, n):
        two[arr[i] + arr[j]] = True

res = 0
for one in range(n):
    for target in range(n):
        if arr[target] - arr[one] in two:
            res = max(res, arr[target])

print(res)