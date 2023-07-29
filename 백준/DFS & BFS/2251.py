from collections import deque
from itertools import permutations

limit = list(map(int, input().split()))
res = set()
res.add(limit[-1])

q = deque()
q.append([0, 0, limit[-1]])
visited = set()
visited.add(tuple([0, 0, limit[-1]]))
while q:
    cur = q.popleft()
    for per in permutations([0, 1, 2], 2):
        temp = cur[:]
        giver, receiver, = per
        if limit[receiver] < temp[receiver] + temp[giver]:
            temp[giver] -= limit[receiver] - temp[receiver]
            temp[receiver] = limit[receiver]
        elif temp[receiver] + temp[giver] <= limit[receiver]:
            temp[receiver] += temp[giver]
            temp[giver] = 0


        if tuple(temp) not in visited:
            visited.add(tuple(temp))
            q.append(temp)
            if temp[0] == 0:
                res.add(temp[-1])

print(*sorted(list(res)))