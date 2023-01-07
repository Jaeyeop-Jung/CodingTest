# TODO 틀림

import sys
from collections import defaultdict
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
a, b, = map(int, input().split())
arrA = [int(input()) for _ in range(a)] * 2
arrB = [int(input()) for _ in range(b)] * 2

dicA = defaultdict(int)
for i in range(a):
    for j in range(1, a):
        dicA[sum(arrA[i:i+j])] += 1
dicB = defaultdict(int)
for i in range(b):
    for j in range(1, b):
        dicB[sum(arrB[i:i+j])] += 1

dicA[0] = 1
dicB[0] = 1
dicA[sum(arrA[:a])] = 1
dicB[sum(arrB[:b])] = 1

result = 0
for i in dicA:
    if n - i in dicB:
        result += dicA[i] * dicB[n - i]
print(result)
