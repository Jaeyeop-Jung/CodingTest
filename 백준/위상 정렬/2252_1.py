from collections import deque, defaultdict

n, m = map(int, input().split())
dic = defaultdict(int)
order = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    dic[v] += 1
    order[u].append(v)

q = deque()
result = []
for i in range(1, n + 1):
    if dic[i] == 0:
        q.append(i)
while q:
    pop = q.popleft()
    result.append(pop)
    if pop in order:
        for after in order[pop]:
            dic[after] -= 1
            if dic[after] == 0:
                q.append(after)

print(*result)