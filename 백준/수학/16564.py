import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

if n == 1:
    print(arr[0] + k)
    exit()

for i in range(1, n):
    nec = i * (arr[i] - arr[i - 1])
    if k < nec:
        i -= 1
        break
    k -= nec

print(arr[i] + k // (i + 1))