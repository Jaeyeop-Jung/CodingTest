from collections import deque

arr = list(map(int, input().split()))
if sum(arr) % 3 != 0:
    print(0)
    exit()
arr.sort()

visited = {}
visited[tuple(arr)] = True
q = deque()
q.append(arr)
while q:
    a, b, c, = q.popleft()
    if a == b == c:
        print(1)
        exit()

    next = tuple(sorted([a * 2, b - a, c]))
    if next not in visited:
        q.append(next)
        visited[next] = True
    next = tuple(sorted([a * 2, b, c - a]))
    if next not in visited:
        q.append(next)
        visited[next] = True
    next = tuple(sorted([a, b * 2, c - b]))
    if next not in visited:
        q.append(next)
        visited[next] = True

print(0)