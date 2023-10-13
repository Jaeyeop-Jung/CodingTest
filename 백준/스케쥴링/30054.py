import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
dic = defaultdict(list)
for _ in range(n):
    book, arrive = map(int, input().split())
    dic[arrive].append(book)
for arrive in dic:
    dic[arrive].sort()

cur = {}
q = deque()
res = 0
for i in range(1, 500_001):
    for book in dic[i]:
        q.append((i, book))
        cur[book] = i

    if i in cur:
        arrive = cur[i]
        del cur[i]
        res = max(res, i - arrive)
    else:
        while q and q[0][1] not in cur:
            q.popleft()
        if q:
            arrive, book = q.popleft()
            del cur[book]
            res = max(res, i - arrive)

# while q:
#     while q and q[0][1] not in cur:
#         q.popleft()
#     if q:
#         book, arrive = q.popleft()
#         res = max()

print(res)