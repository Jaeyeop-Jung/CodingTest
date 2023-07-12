# TODO 틀림 다음엔 좀 맞자

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dic = defaultdict(int)
for i in arr:
    dic[i] += 1

cntArr = [dic[i] for i in arr]
stack = []
res = [-1] * n
for i in range(n):
    while stack and stack[-1][0] < cntArr[i]:
        res[stack.pop()[1]] = arr[i]
    stack.append([cntArr[i], i])

print(*res)