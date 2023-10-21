
def getMinSumNodeValues(service_nodes, service_from, service_to, k, currentValues):
    graph = [[] for _ in range(service_nodes)]
    nodes = [0] * service_nodes
    for i in range(len(service_from)):
        graph[service_from[i] - 1].append(service_to[i] - 1)
        graph[service_to[i] - 1].append(service_from[i] - 1)
    for i, v in currentValues:
        nodes[i - 1] = v





print(getMinSumNodeValues(
    4, 3, [1, 2, 2], [2, 3, 4], 3, [[1, 3], [2, 4], [3, 3]]
))