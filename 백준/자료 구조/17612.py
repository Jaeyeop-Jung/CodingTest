import random
import sys
import heapq

input = sys.stdin.readline

n, k, = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# n, k = 100_000, 1000
# arr = [[random.randrange(1, 1000000), random.randrange(1, 20)] for _ in range(n)]

res = []
counter = []

# 초기 투입
cnt = 1
for i in range(min(n, k)):
    heapq.heappush(counter, (arr[i][1], arr[i][0], cnt))
    cnt += 1

# 진행
time = 0
idx = min(n, k)
while counter:
    enter = []
    out = []
    cost, id, counterNum, = heapq.heappop(counter)
    heapq.heappush(out, [-counterNum, id])
    heapq.heappush(enter, counterNum)
    time = cost

    while counter and counter[0][0] == cost:
        cost, id, counterNum, = heapq.heappop(counter)
        heapq.heappush(out, [-counterNum, id])
        heapq.heappush(enter, counterNum)

    while idx < n and enter:
        cnt = heapq.heappop(enter)
        heapq.heappush(counter, (arr[idx][1] + time, arr[idx][0], cnt))
        idx += 1

    while out:
        res.append(heapq.heappop(out)[1])

print(sum((i + 1) * res[i] for i in range(len(res))))