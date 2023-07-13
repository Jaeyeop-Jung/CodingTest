# TODO 틀림 맞출 수 있다 잘 생각해봐

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


n, q, = map(int, input().split())
arr = []
for i in range(n):
    arr.append([i] + list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[2]))
parent = [i for i in range(n)]
for i in range(n - 1):
    if arr[i][1] <= arr[i + 1][1] <= arr[i][2]:
        union_parent(parent, arr[i][0], arr[i + 1][0])

for i in range(n):
    find_parent(parent, i)

for _ in range(q):
    left, right = map(int, input().split())
    if parent[left - 1] == parent[right - 1]:
        print(1)
    else:
        print(0)