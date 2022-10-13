# TODO 틀림 구현을 더 깊게 생각

import sys

sys.setrecursionlimit(10 ** 6)

result = []

def insert(nodeinfo, graph, parent, idx, x, y):
    if None not in graph[parent]:
        if nodeinfo[parent][0] < x:
            insert(nodeinfo, graph, graph[parent][1], idx, x, y)
        else:
            insert(nodeinfo, graph, graph[parent][0], idx, x, y)
        return
    if x < nodeinfo[parent][0]:
        if graph[parent][0] == None:
            graph[parent][0] = idx
        else:
            insert(nodeinfo, graph, graph[parent][0], idx, x, y)
        return
    else:
        if graph[parent][1] == None:
            graph[parent][1] = idx
        else:
            insert(nodeinfo, graph, graph[parent][1], idx, x, y)
        return

def preOrder(graph, root):
    global result
    temp.append(root + 1)
    if graph[root][0] is not None:
        preOrder(graph, graph[root][0])
    if graph[root][1] is not None:
        preOrder(graph, graph[root][1])

def postOrder(graph, root):
    global result
    if graph[root][0] is not None:
        postOrder(graph, graph[root][0])
    if graph[root][1] is not None:
        postOrder(graph, graph[root][1])
    temp.append(root + 1)

def solution(nodeinfo):
    n = len(nodeinfo)
    sortedNodeInfo = [[i, nodeinfo[i][0], nodeinfo[i][1]] for i in range(n)]
    sortedNodeInfo.sort(key=lambda x:(-x[2], x[1]))
    graph = [[None, None] for i in range(n)]
    for i in range(1, n):
        insert(nodeinfo, graph, sortedNodeInfo[0][0], sortedNodeInfo[i][0], sortedNodeInfo[i][1], sortedNodeInfo[i][2])

    global result
    result = []
    preOrder(graph, sortedNodeInfo[0][0])
    result.append(temp)
    temp = []
    postOrder(graph, sortedNodeInfo[0][0])
    result.append(temp)

    return result

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))