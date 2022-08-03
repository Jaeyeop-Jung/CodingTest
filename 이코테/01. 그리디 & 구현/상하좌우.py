import sys

input = sys.stdin.readline

dDirection = ['R', 'L', 'D', 'U']
dRow = [0, 0, 1, -1]
dColumn = [1, -1, 0, 0]

curRow, curColumn = 1, 1

n = int(input())
direction = list(input().split())
for i in direction:
    index = dDirection.index(i)
    if not (1 <= curRow + dRow[index] <= n) or not (1 <= curColumn + dColumn[index] <= n):
        continue
    curRow += dRow[index]
    curColumn += dColumn[index]

print(curRow, curColumn)