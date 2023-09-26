import sys
from collections import defaultdict

input = sys.stdin.readline

n, m, = map(int, input().split())
t = int(input())
arr = [list(map(int, input().split())) for _ in range(t)]

arr.sort(key=lambda x: (x[0], x[1], x[2]))
cur = 0
res = 0
dic = defaultdict(int)
for i in range(t):
    start, end, weight, = arr[i]
    keys = sorted(list(dic.keys()))
    for key in keys:
        if key <= start:
            res += dic[key]
            cur -= dic[key]
            del dic[key]

    if cur + weight <= m:
        dic[end] += weight
        cur += weight
    else:
        keys = sorted(list(dic.keys()))
        tempWeight = 0
        while keys and end < keys[-1]:
            popNum = keys.pop()
            if cur - dic[popNum] + weight <= m:
                restWeight = m - (cur - dic[popNum] + weight)
                cur -= dic[popNum] - restWeight
                dic[popNum] = restWeight
                break
            else:
                cur -= dic[popNum]
                del dic[popNum]
        dic[end] += m - cur
        cur = m

print(res + sum([dic[key] for key in dic]))