import sys
from collections import defaultdict

input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    clothes = defaultdict(list)
    for _ in range(n):
        name, kind = input().split()
        clothes[kind].append(name)
    res = 1
    for kind in clothes:
        res *= (len(clothes[kind]) + 1)
    print(res - 1)

