import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
        res[a] += res[b]
        print(res[a])
    elif a > b:
        parent[a] = b
        res[b] += res[a]
        print(res[b])
    else:
        print(res[b])


t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    res = []
    dic = {}
    parent = []
    for _ in range(n):
        a, b, = input().rstrip().split()
        if a not in dic:
            dic[a] = cnt
            parent.append(cnt)
            cnt += 1
            res.append(1)
        if b not in dic:
            dic[b] = cnt
            parent.append(cnt)
            cnt += 1
            res.append(1)
        union_parent(parent, dic[a], dic[b])
