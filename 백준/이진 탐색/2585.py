import math
import sys
import heapq

input = sys.stdin.readline

n, k, = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)] + [[10000, 10000]]

def dijkstra(gas):
    h = [[-1, 0]]
    cnt = [math.inf] * (n + 2)
    cnt[0] = -1
    while h:
        cost, cur, = heapq.heappop(h)
        for next in range(len(arr)):
            if gas * 10 < ((arr[cur][0] - arr[next][0]) ** 2 + (arr[cur][1] - arr[next][1]) ** 2) ** 0.5:
                continue
            if cnt[next] <= cost + 1:
                continue
            heapq.heappush(h, [cost + 1, next])
            cnt[next] = cost + 1
    return cnt[-1]

left, right = 0, 1415
while left <= right:
    mid = (left + right) // 2
    temp = dijkstra(mid)
    if temp <= k:
        right = mid - 1
        res = mid
    else:
        left = mid + 1

print(res)