import sys

input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(input().split()))
    graph[i].append(i)

graph.sort(key=lambda x: (int(x[0]), x[2]))
for i in graph:
    print(i[0], i[1])