import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)
result = arr[0]
for i in range(1, len(arr)):
    result = max(result, arr[i] * (i + 1))

print(result)