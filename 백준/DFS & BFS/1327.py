from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

visited = {}
visited[tuple(arr)] = 0
q = deque()
q.append([list(arr), 0])
while q:
    pop, cost = q.popleft()
    for i in range(n):
        if i + k <= n:
            newArr = pop[:i] + list(reversed(pop[i:i + k])) + pop[i + k:]
            if tuple(newArr) not in visited:
                visited[tuple(newArr)] = cost + 1
                q.append([newArr, cost + 1])

res = tuple([i for i in range(1, n + 1)])
print(visited[res] if res in visited else -1)
