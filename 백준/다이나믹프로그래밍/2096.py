import math
import sys

input = sys.stdin.readline

dC = [-1, 0, 1]

n = int(input())
initArr = list(map(int, input().split()))
dpMax = initArr
dpMin = initArr
for _ in range(n - 1):
    nextArr = list(map(int, input().split()))
    nextDpMax = [0] * 3
    nextDpMin = [math.inf] * 3
    for c in range(3):
        for i in range(3):
            nextC = c + dC[i]
            if not 0 <= nextC < 3:
                continue
            nextDpMax[nextC] = max(nextDpMax[nextC], dpMax[c] + nextArr[nextC])
            nextDpMin[nextC] = min(nextDpMin[nextC], dpMin[c] + nextArr[nextC])
    dpMax = nextDpMax
    dpMin = nextDpMin

print(max(dpMax), min(dpMin))