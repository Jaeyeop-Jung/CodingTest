import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

maxi = max(arr)
idx = arr.index(maxi)
arr.pop(idx)
result = 0
for i in arr:
    result += maxi + i

print(result)
