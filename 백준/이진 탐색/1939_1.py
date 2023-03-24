# TODO 틀림

from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    u, v, w, = map(int, input().split())
    arr[u - 1].append([v - 1, w])
    arr[v - 1].append([u - 1, w])
start, end = map(int, input().split())

for i in arr:
    i.sort(key=lambda x: -x[1])

def go(canWeight, start, end):
    q = deque()
    q.append(start)
    visited = [False] * n
    visited[start] = True
    while q:
        cur = q.popleft()
        for next, cost in arr[cur]:
            if visited[next]:
                continue
            if canWeight <= cost:
                q.append(next)
                visited[next] = True
                if next == end:
                    return True
    return False

left, right = 1, 1000000000
result = 0
while left <= right:
    mid = (left + right) // 2
    if go(mid, start - 1, end - 1):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)