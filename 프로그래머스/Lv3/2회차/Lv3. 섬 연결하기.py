
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


def solution(n, costs):
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[2])
    result = 0
    for u, v, w in costs:
        if find_parent(parent, u) == find_parent(parent, v):
            continue
        union_parent(parent, u, v)
        result += w
    return result

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))


