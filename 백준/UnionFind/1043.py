# TODO 틀림 할 수 있어 잘 생각해봐

import sys
input = sys.stdin.readline

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


n, m, = map(int, input().split())
# member = [[i, set()] for i in range(n + 1)]
# known = list(map(int, input().split()))
# for i in range(1, len(known)):
#     member[known[i]][0] = 0
#
# for num in range(1, m + 1):
#     flag = False
#     party = list(map(int, input().split()))
#     for i in range(1, len(party)):
#         member[party[i]][1].add(num)
#         if member[party[i]][0] == 0:
#             flag = True
#             break
#     if flag:
#         for i in range(1, len(party)):
#             member[party[i]][0] = 0
#             member[party[i]][1].add(num)
#
# partyNum = set()
# for i, s in member:
#     if i == 0:
#         partyNum |= s
#
# print(m - len(partyNum))

parent = [i for i in range(n + 1)]
parties = [[] for _ in range(n + 1)]
known = list(map(int, input().split()))
for i in range(m):
    party = list(map(int, input().split()))
    for j in range(1, len(party)):
        parties[party[j]].append(i)
    if 2 <= party[0]:
        for j in range(1, len(party) - 1):
            union_parent(parent, party[j], party[j + 1])

for i in range(1, len(parent)):
    find_parent(parent, i)

known = known[1:]
for i in range(len(known)):
    known[i] = find_parent(parent, known[i])

result = set()
for i in range(1, len(parent)):
    if parent[i] in known:
        for j in parties[i]:
            result.add(j)
print(m - len(result))
