import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
flight = [int(input()) for _ in range(m)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

parent = [i for i in range(n + 1)]

cnt = 0
for cur in flight:
    gate = find_parent(parent, cur)
    if gate == 0:
        break
    parent[gate] = find_parent(parent, gate - 1)
    cnt += 1

print(cnt)