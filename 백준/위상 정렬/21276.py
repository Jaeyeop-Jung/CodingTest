# TODO 틀림

# from collections import deque
from collections import defaultdict
import heapq

n = int(input())
people = list(input().split())
people.sort()
m = int(input())
degree = defaultdict(int)
way = defaultdict(list)
for _ in range(m):
    x, y, = input().split()
    degree[x] += 1
    way[y].append(x)

# q = deque()
h = []
starter = []
for key in people:
    if degree[key] == 0:
        # q.append(key)
        heapq.heappush(h, key)
        starter.append(key)

family = defaultdict(list)
while h:
    pop = heapq.heappop(h)
    for next in way[pop]:
        degree[next] -= 1
        if degree[next] == 0:
            family[pop].append(next)
            # q.append(next)
            heapq.heappush(h, next)

# starter = people[:]
# for key in family:
#     for child in family[key]:
#         starter.remove(child)

print(len(starter))
print(*starter)
pr = sorted(list(people))
for person in pr:
    print(f'{person} {len(family[person])} ', end='')
    print(*sorted(family[person]))
