# TODO 틀림 잘 생각해봐라

import sys
input = sys.stdin.readline

def dfs(arr, visited, start, cur, route):
    if visited[cur]:
        global result
        if cur in route:
            result += len(route[route.index(cur):])
        return
    visited[cur] = True
    dfs(arr, visited, start, arr[cur] - 1, route + [cur])

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    visited = [False] * n
    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            dfs(arr, visited, i, arr[i] - 1, [i])
    print(n - result)

    # visited_node = {}
    # for i in range(len(arr)):
    #     if i in visited_node:
    #         continue
    #     visited = [False] * len(arr)
    #     visited[i] = True
    #     next = arr[i] - 1
    #     count = 1
    #     while True:
    #         if visited[next]:
    #             if next == i:
    #                 result += count
    #                 for i, v in enumerate(visited):
    #                     if v:
    #                         visited_node[i] = True
    #                 break
    #             break
    #         visited[next] = True
    #         next = arr[next] - 1
    #         count += 1
    # print(n - result)