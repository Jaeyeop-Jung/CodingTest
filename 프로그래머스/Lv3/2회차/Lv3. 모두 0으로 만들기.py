# TODO 틀림
#
# from collections import deque
#
# def solution(a, edges):
#     if sum(a) != 0:
#         return -1
#     parent = [i for i in range(len(a))]
#     edges.sort(key=lambda x: x[0])
#     for index, j in edges:
#         if parent[index] < parent[j]:
#             parent[j] = index
#         else:
#             parent[index] = j
#
#     result = 0
#     maxi = max(parent)
#     q = deque([i for i in range(len(parent)) if parent[i] == maxi])
#     while q:
#         index = q.popleft()
#         while a[index] != 0:
#             temp = a[index]
#             if temp < 0:
#                 a[index] += temp
#                 a[parent[index]] -= temp
#             else:
#                 a[index] -= temp
#                 a[parent[index]] += temp
#             result += temp
#         if parent[index] == index:
#             break
#         q.append(parent[index])
#
#     return result

import sys
sys.setrecursionlimit(300000)
from collections import defaultdict
answer = 0

def dfs(x, a, tree, visited):
    global answer
    visited[x] = 1

    for y in tree[x]:
        if not visited[y]:
            a[x] += dfs(y, a, tree, visited)
    answer += abs(a[x])

    return a[x]


def solution(a, edges):
    global answer

    if sum(a) != 0:
        return -1

    tree = defaultdict(list)
    for i, j in edges:
        tree[i].append(j)
        tree[j].append(i)

    visited = [0]*(len(a))

    dfs(0, a, tree, visited)

    return answer


print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))
print(solution([0,1,0], [[0,1],[1,2]]))
