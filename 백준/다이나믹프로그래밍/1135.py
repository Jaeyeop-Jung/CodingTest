# TODO 틀림

from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

tree = defaultdict(list)
for cur, parent in enumerate(arr):
    tree[parent].append(cur)

# visited = [False] * n
# visited[0] = True
# called = [0]
# result = 0
# while False in visited:
#     temp = []
#     for cur in called:
#         if tree[cur]:
#             next = tree[cur][0]
#             nextSize = len(tree[tree[cur][0]])
#             for nextKey in tree[cur]:
#                 if nextSize < len(tree[nextKey]):
#                     next = nextKey
#                     nextSize = len(tree[nextKey])
#             visited[next] = True
#             tree[cur].remove(next)
#             temp.append(next)
#     called.extend(temp)
#     result += 1




print(result)