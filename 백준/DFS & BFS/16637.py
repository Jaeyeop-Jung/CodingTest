# TODO 틀림

import math

n = int(input())
s = input()

def cal(a, b, op):
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def dfs(s, idx, cur):
    if len(s) <= idx:
        global res
        res = max(res, cur)
        return

    # 괄호 하기
    dfs(s, idx + 2, cal(cur, s[idx + 1], s[idx]))

    # 다음에 괄호 하기
    if idx + 3 <= len(s):
        dfs(s, idx + 4, cal(cur, cal(s[idx + 1], s[idx + 3], s[idx + 2]), s[idx]))

res = -math.inf
dfs(s, 1, int(s[0]))
print(res)