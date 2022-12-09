import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())

result = []
resCnt = 0
for c in range(m):
    dic = defaultdict(int)
    for r in range(n):
        dic[arr[r][c]] += 1
    temp = sorted([[k, dic[k]] for k in dic], key=lambda x: (-x[1], x[0]))
    resCnt += sum([temp[i][1] for i in range(1, len(temp))])
    result.append(temp[0][0])

print(''.join(result))
print(resCnt)