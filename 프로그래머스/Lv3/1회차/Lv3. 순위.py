# TODO 틀림 아이디어도 못 떠올림

def solution(n, results):
    graph = [[None] * n for i in range(n)]
    idx = 0
    while idx < n:
        graph[idx][idx] = True
        idx += 1
    for win, lose in results:
        graph[win - 1][lose - 1] = True
        graph[lose - 1][win - 1] = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[i][k] is True and graph[k][j] is True:
                    graph[i][j] = True
                elif graph[i][k] is False and graph[k][j] is False:
                    graph[i][j] = False

    return len([i for i in range(len(graph)) if None not in graph[i]])

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))