import math
import sys
from collections import defaultdict

input = sys.stdin.readline

def getDiff(s1, s2):
    cnt = 0
    for i in range(4):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt

def dfs(dic, cur):
    if len(cur) == 3:
        global res
        res = min(res, getDiff(cur[0], cur[1]) + getDiff(cur[0], cur[2]) + getDiff(cur[1], cur[2]))
        return

    for key in dic:
        if 0 < dic[key]:
            dic[key] -= 1
            dfs(dic, cur + [key])
            dic[key] += 1


t = int(input())
for _ in range(t):
    n = int(input())
    res = math.inf
    dic = defaultdict(int)

    arr = list(input().split())
    for i in range(n):
        dic[arr[i]] += 1

    dfs(dic, [])
    print(res)
