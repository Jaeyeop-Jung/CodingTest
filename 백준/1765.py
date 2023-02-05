
n = int(input())
m = int(input())

friend = [[] for _ in range(n)]
enemy = [[] for _ in range(n)]
for _ in range(m):
    s, a, b, = input().split()
    a, b = int(a) - 1, int(b) - 1
    if s == 'F':
        friend[a].append(b)
        friend[b].append(a)
    else:
        enemy[a].append(b)
        enemy[b].append(a)

# team = [set() for i in range(n)]
# for i in range(len(team)):
#     team[i].add(i)
# for cur in range(len(friend)):
#     for next in friend[cur]:
#         team[cur].add(next)
#         team[next].add(cur)
#         for frToFr in friend[next]:
#             team[cur] |= team[frToFr]
#             team[frToFr] |= team[cur]
#
# for cur in range(len(enemy)):
#     for next in enemy[cur]:
#         # 적의 적은 친구
#         for enemyToEnemy in enemy[next]:
#             team[cur] |= team[enemyToEnemy]
#             team[enemyToEnemy] |= team[cur]
#
# result = [i for i in range(n)]
# for i in range(len(team)):
#     for j in team[i]:
#         result[j] = min(result[j], result[i])
#         result[i] = min(result[j], result[i])
#
# print(len(set(result)))

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

parent = [i for i in range(n)]
for cur in range(len(friend)):
    for next in friend[cur]:
        union_parent(parent, cur, next)
        for frToFr in friend[next]:
            union_parent(parent, cur, frToFr)

for cur in range(len(enemy)):
    for next in enemy[cur]:
        # 적의 적은 친구
        for enemyToEnemy in enemy[next]:
            union_parent(parent, cur, enemyToEnemy)

for i in range(len(parent)):
    find_parent(parent, i)

print(len(set(parent)))