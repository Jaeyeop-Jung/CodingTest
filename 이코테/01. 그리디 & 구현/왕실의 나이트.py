import sys
from string import ascii_lowercase

dRow = [-1, 1, 2, 2, 1, -1, -2, -2]
dColumn = [2, 2, 1, -1, -2, -2, -1, 1]

input = sys.stdin.readline

list = list(ascii_lowercase)
n = input()

curRow = int(n[1])
curColumn = list.index(n[0]) + 1

result = 0
for i in range(len(dRow)):
    if not (1 <= curRow + dRow[i] <= 8) or not (1 <= curColumn + dColumn[i] <= 8):
        continue
    result += 1

print(result)