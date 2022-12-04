import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

result = 0
for i in permutations(arr, len(arr)):
    temp = 0
    for j in range(len(i) - 1):
        temp += abs(i[j] - i[j + 1])
    result = max(result, temp)
    if temp == 11:
        print(i)

print(result)
