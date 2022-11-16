import math
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [i for i in range(0, 10)]
if m != 0:
    wrong = list(map(int, input().split()))
    for i in wrong:
        arr.remove(i)

result = abs(n - 100)
def dfs(num):
    if 6 < len(num):
        return
    global result
    result = min(result, abs(n - int(num)) + len(num))
    for i in arr:
        dfs(num + str(i))

for i in arr:
    dfs(str(i))
print(result)