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
    else:
        parent[a] = b


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    k = int(input())

    parent = [i for i in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    print(f'Scenario {tc}:')
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if find_parent(parent, a) == find_parent(parent, b):
            print(1)
        else:
            print(0)
    print()