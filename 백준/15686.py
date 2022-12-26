import math
from itertools import combinations
import sys
input = sys.stdin.readline

dRow = [0, 1, 0, -1]
dColumn = [1, 0, -1, 0]

n, m = map(int, input().split())
house = []
chicken = []
arr = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            house.append([i, j])
        if temp[j] == 2:
            chicken.append([i, j])
    arr.append(temp)

result = math.inf
for case in combinations(chicken, m):
    temp = 0
    for houseR, houseC in house:
        tempC = math.inf
        for chickenR, chickenC in case:
            tempC = min(tempC, abs(houseR - chickenR) + abs(houseC - chickenC))
        temp += tempC

    result = min(result, temp)

print(result)