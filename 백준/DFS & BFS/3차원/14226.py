import math
from collections import deque

n = int(input())
dp = [[math.inf] * 1001 for _ in range(1001)]
dp[1][0] = 0

q = deque()
q.append([1, 0, 0])
while q:
    num, cnt, copy = q.popleft()

    # 1
    if cnt + 1 < dp[num][num]:
        dp[num][num] = cnt + 1
        q.append([num, cnt + 1, num])

    # 2
    if num + copy <= 1000 and cnt + 1 < dp[num + copy][copy]:
        dp[num + copy][copy] = cnt + 1
        q.append([num + copy, cnt + 1, copy])

    # 3
    if 0 < num - 1 and cnt + 1 < dp[num - 1][copy]:
        dp[num - 1][copy] = cnt + 1
        q.append([num - 1, cnt + 1, copy])

print(min(dp[n]))

