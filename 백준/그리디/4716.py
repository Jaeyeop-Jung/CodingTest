# TODO 틀림

import sys

input = sys.stdin.readline

while True:
    n, a, b, = map(int, input().split())
    if n == 0 and a == 0 and b == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[0] * b for _ in range(a)] for _ in range(n)]
    print()

