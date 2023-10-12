# TODO 틀림

def canHotel(cur, curCost):
    for i in range(n):
        if kind[i][0] == 'H' and curCost + graph[cur][i] <= 540:
            return True
    return False


def dfs(graph, kind, day, minute, route, happy, visited):
    if day == m + 1:
        global res, resRoute
        if res < happy:
            res = happy
            resRoute = route[:]
        return

    cur = route[-1]
    go = False
    for next in range(n):
        if visited[next] or next == cur or kind[next][0] == 'A' or kind[next][0] == 'H':
            continue
        if minute + graph[cur][next] + kind[next][1] <= 540 and canHotel(next, minute + graph[cur][next] + kind[next][1]):
            visited[next] = True
            route.append(next)
            dfs(graph, kind, day, minute + graph[cur][next] + kind[next][1], route, happy + kind[next][2], visited)
            visited[next] = False
            route.pop()
            go = True

    if not go:
        if day == 5:
            if minute + graph[cur][route[0]] <= 540:
                route.append(route[0])
                dfs(graph, kind, day + 1, 0, route, happy, visited)
                route.pop()
        else:
            for hotel in range(n):
                if kind[hotel][0] != 'H':
                    continue
                if minute + graph[cur][hotel] <= 540:
                    route.append(hotel)
                    dfs(graph, kind, day + 1, 0, route, happy, visited)
                    route.pop()

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[0] * n for _ in range(n)]
    for u in range(n - 1):
        temp = list(map(int, input().split()))
        for i in range(len(temp)):
            v = i + u + 1
            graph[u][v] = temp[i]
            graph[v][u] = temp[i]

    kind = [list(input().split()) for _ in range(n)]
    start = -1
    for i in range(n):
        if kind[i][0] == 'P':
            kind[i][1], kind[i][2] = int(kind[i][1]), int(kind[i][2])
        elif kind[i][0] == 'A':
            start = i

    res = 0
    resRoute = []
    dfs(graph, kind, 1, 0, [start], 0, [False] * n)

    resRoute = [i + 1 for i in resRoute] + [start + 1]
    print(f'#{tc} {res} ', end='')
    print(*resRoute[1:])