import math

n = int(input())
arr = list(map(int, input().split()))

dpLeft = [-math.inf] * n
dpRight = [-math.inf] * n
dpLeft[0] = 1 if arr[0] == 1 else 0
dpRight[0] = 1 if arr[0] == 2 else 0
for i in range(1, n):
    if arr[i] == 1:
        dpLeft[i] = max(dpLeft[i], dpLeft[i - 1] + 1)
    else:
        dpLeft[i] = max(0, dpLeft[i - 1] - 1)

    if arr[i] == 2:
        dpRight[i] = max(dpRight[i], dpRight[i - 1] + 1)
    else:
        dpRight[i] = max(0, dpRight[i - 1] - 1)

print(max(max(dpLeft), max(dpRight)))