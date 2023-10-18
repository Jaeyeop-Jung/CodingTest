import sys
from collections import deque

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 4)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n):
    a, b, = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

def recur(graph, visited, start, cur, pre):
    for next in graph[cur]:
        # 싸이클 찾음
        if next == start and pre != next:
            for i in range(n):
                if visited[i]:
                    print(0, end=' ')
                else:
                    q = deque()
                    q.append((i, 0))
                    tempVisited = [False] * n
                    tempVisited[i] = True
                    while q:
                        cur, cost, = q.popleft()
                        for next in graph[cur]:
                            if tempVisited[next]:
                                continue
                            if visited[next]:
                                print(cost + 1, end=' ')
                                break
                            tempVisited[next] = True
                            q.append((next, cost + 1))
            exit()
        else:
            if not visited[next]:
                visited[next] = True
                recur(graph, visited, start, next, cur)
                visited[next] = False



visited = [False] * n
for start in range(n):
    visited[start] = True
    recur(graph, visited, start, start, start)
    visited[start] = False