import math
import heapq

n = int(input())
arr = list(map(int, input().split()))

dp = [math.inf] * n
dp[0] = 0
h = [[0, 0]]
while h:
    cost, cur, = heapq.heappop(h)
    if dp[cur] < cost:
        continue
    for i in range(cur + 1, cur + arr[cur] + 1):
        if n <= i:
            continue
        if cost + 1 < dp[i]:
            heapq.heappush(h, [cost + 1, i])
            dp[i] = cost + 1

print(dp[-1] if dp[-1] != math.inf else -1)

