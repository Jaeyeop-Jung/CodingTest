import heapq

n = int(input())
time = [0] * 1_000_002
arr = []
for _ in range(n):
    start, end, = map(int, input().split())
    time[start] += 1
    time[end + 1] -= 1
    arr.append([start, end])

cur = 0
for i in range(len(time)):
    cur += time[i]
    time[i] = cur
minPC = max(time)

arr.sort(key=lambda x: (-x[0], -x[1]))
h = []
usePC = [0] * minPC
pcNum = [i for i in range(minPC)]
while arr:
    start, end, = arr.pop()
    while h and h[0][0] <= start:
        heapq.heappush(pcNum, heapq.heappop(h)[2])
    pc = heapq.heappop(pcNum)
    heapq.heappush(h, [end, start, pc])
    usePC[pc] += 1

print(minPC)
print(*usePC)