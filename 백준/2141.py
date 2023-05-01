# TODO 틀림

import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x, a, = map(int, input().split())
    arr.append([x, a])
arr.sort()
