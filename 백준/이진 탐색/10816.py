import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
findArr = list(map(int, input().split()))

arr.sort()
result = []
for i in findArr:
    result.append(bisect_right(arr, i) - bisect_left(arr, i))

for i in result:
    print(i, end=' ')