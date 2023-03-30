import heapq

n, t = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def isAvailable(mid):
    h = []
    for i in range(mid):
        heapq.heappush(h, arr[i])
    time = 0
    for i in range(mid, len(arr)):
        time = heapq.heappop(h)
        heapq.heappush(h, arr[i] + time)
    while h:
        time = max(time, heapq.heappop(h))
    return time <= t


start, end = 1, n
while start <= end:
    mid = (start + end) // 2
    if isAvailable(mid):
        end = mid - 1
    else:
        start = mid + 1

print(start)