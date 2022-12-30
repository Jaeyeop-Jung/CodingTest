import math
import sys

input = sys.stdin.readline

def bf(start):
    dist = [int(1e9)] * (n + 1)
    dist[start] = 0
    for i in range(n):
        for edge in graph:
            cur, next, cost, = edge
            if dist[cur] + cost < dist[next]:
                dist[next] = dist[cur] + cost
                if i == n - 1:
                    return True
    return False


t = int(input())
for _ in range(t):
    n, m, w, = map(int, input().split())
    graph = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph.append([a, b, c])
        graph.append([b, a, c])
    for _ in range(w):
        a, b, c = map(int, input().split())
        graph.append([a, b, -c])

    if bf(1):
        print('YES')
    else:
        print('NO')
