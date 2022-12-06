# TODO 틀림 

import math
from collections import defaultdict

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dic = defaultdict(int)
for i in arr:
    dic[i] += 1

cur = []
result = 0
for i in range(len(arr)):
    if arr[i] in cur:
        pass
    elif len(cur) < n:
        cur.append(arr[i])
    else:
        result += 1
        mini, minidx = math.inf, math.inf
        for j in range(len(cur)):
            if dic[cur[j]] < mini:
                mini = dic[cur[j]]
                minidx = j
        cur.pop(minidx)
        cur.append(arr[i])
    dic[arr[i]] -= 1

print(result)