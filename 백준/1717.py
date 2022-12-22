# TODO 틀림 풀 수 있다

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
cmd = [list(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n + 1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for c, u, v in cmd:
    if c == 0:
        union_parent(parent, u, v)
    else:
        if find_parent(parent, u) == find_parent(parent, v):
            print('YES')
        else:
            print('NO')