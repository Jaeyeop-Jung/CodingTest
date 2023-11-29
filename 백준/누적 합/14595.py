import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]
#
# def union_parent(parent, x, y):
#     a = find_parent(parent, x)
#     b = find_parent(parent, y)
#     if a < b:
#         parent[a] = b
#     else:
#         parent[b] = a
#
# parent = [i for i in range(n + 1)]
# for i in range(m):
#     a, b, = map(int, input().split())

prefix = [0] * (n + 1)
for i in range(m):
    a, b, = map(int, input().split())
    prefix[a] += 1
    prefix[b] -= 1

res = 0
cur = 0
for i in range(1, len(prefix)):
    if prefix[i] == 0 and cur == 0:
        res += 1
    elif prefix[i] == 0 and cur != 0:
        continue
    elif prefix[i] < 0:
        cur += prefix[i]
        if cur == 0:
            res += 1
    else:
        cur += prefix[i]

print(res)