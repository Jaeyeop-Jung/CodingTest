# TODO 틀림 이분 그래프 잘 기억해라

from collections import deque
import sys
input = sys.stdin.readline

dic = {
    'R': 'B',
    'B': 'R'
}

def bfs(visited, start):
    q = deque()
    q.append([start, 'R'])
    visited[start] = 'R'
    flag = False
    while q:
        cur, group, = q.popleft()
        for next in graph[cur]:
            if visited[next] == 'N':
                visited[next] = dic[group]
                q.append([next, dic[group]])
            elif visited[next] != 'N' and visited[next] == group:
                flag = True
                break
        if flag:
            break
    if flag:
        return False
    else:
        return True


t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        c, n = map(int, input().split())
        graph[c - 1].append(n - 1)
        graph[n - 1].append(c - 1)

    if v == 1:
        print('YES')
        continue

    q = deque()
    q.append([0, 'R'])
    visited = ['N'] * v
    result = True
    for node in range(len(visited)):
        if visited[node] == 'N':
            result = bfs(visited, node)
            if result == False:
                break
    if result:
        print('YES')
    else:
        print('NO')
