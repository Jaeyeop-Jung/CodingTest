import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    heapq.heapify(arr)
    cost = 0
    while len(arr) != 1:
        temp = heapq.heappop(arr) + heapq.heappop(arr)
        cost += temp
        heapq.heappush(arr, temp)

    print(cost)
