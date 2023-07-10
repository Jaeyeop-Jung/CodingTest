import math


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

def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n - 1)]

parent = [i for i in range(n)]
graph = [[] for _ in range(n)]

for i in range(n - 1):
    a, b, c1, c2, = arr[i]
    union_parent(parent, a, b)
    graph[a].append([b, c1, c2])
    graph[b].append([a, c2, c1])

for i in range(n):
    find_parent(parent, i)

superParent = parent[0]
cost = [[1, 1] for _ in range(n)]
visited = [False] * n
def dfs(graph, visited, cur, op1, op2):
    for next, c1, c2 in graph[cur]:
        if visited[next]:
            continue
        visited[next] = True
        cost[next] = [op1 * c1, op2 * c2]
        dfs(graph, visited, next, op1 * c1, op2 * c2)

visited[superParent] = True
dfs(graph, visited, superParent, 1, 1)

lcmScore = 1
for i, j in cost:
    lcmScore = lcm(lcmScore, i)

for i in range(len(cost)):
    cost[i] = (lcmScore * cost[i][1]) // cost[i][0]

gcd = cost[0]
for i in range(1, len(cost)):
    gcd = math.gcd(gcd, cost[i])
for i in cost:
    print(i // gcd, end=' ')