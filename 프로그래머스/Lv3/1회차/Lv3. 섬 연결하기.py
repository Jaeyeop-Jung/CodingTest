# TODO 틀림

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] =  find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = find_parent(parent, a)
    else:
        parent[a] = find_parent(parent, b)

def solution(n, costs):
    result = 0
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    for start, end, cost in costs:
        if find_parent(parent, start) == find_parent(parent, end):
            continue
        else:
            result += cost
            union_parent(parent, start, end)
    return result

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))