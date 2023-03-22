import math
from collections import deque

q = deque(list(input()))

result = math.inf
for _ in range(len(q)):
    q.rotate(1)
    temp = ''
    cur = q[0]
    cnt = 1
    for i in range(1, len(q)):
        if cur == q[i]:
            cnt += 1
            continue
        temp += cur + str(cnt)
        cnt = 1
        cur = q[i]
    temp += cur + str(cnt)
    result = min(result, len(temp))

print(result)
