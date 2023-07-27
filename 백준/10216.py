
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
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = ((arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2)
            if dist <= (arr[i][2] + arr[j][2]) ** 2:
                union_parent(parent, i, j)

    for i in range(n):
        find_parent(parent, i)

    print(len(set(parent)))