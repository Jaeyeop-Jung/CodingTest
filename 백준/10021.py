# TODO 틀림 아이디어는 완전 맞았는데 메모리 초과 해결법을 못찾음..

import sys
import heapq
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

n, c, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

distance = []
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        dist = (arr[i][0] - arr[j][0]) ** 2 + (arr[i][1] - arr[j][1]) ** 2
        if dist < c:
            continue
        heapq.heappush(distance, [dist, i, j])

parent = [i for i in range(n)]
result, cnt = 0, 0
while distance:
    w, u, v = heapq.heappop(distance)
    if find_parent(parent, u) != find_parent(parent, v):
        union_parent(parent, u, v)
        result += w
        cnt += 1
    if cnt == n - 1:
        break
print(result if n - 1 <= cnt else -1)
