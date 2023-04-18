# TODO 틀림

import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    cnt = 0
    while 0 < n - cnt * 10:
        arr += list(map(int, input().split()))
        cnt += 1

    result = []
    mid = arr[0]
    result.append(mid)

    maxH = []
    minH = []
    for i in range(1, n):
        # 값 넣기
        if i % 2 == 1:
            if mid < arr[i]:
                heapq.heappush(minH, arr[i])
            else:
                heapq.heappush(maxH, -arr[i])
        # 중앙값 찾기
        else:
            if len(maxH) < len(minH):
                pop = heapq.heappop(minH)
            else:
                pop = -heapq.heappop(maxH)

            temp = sorted([mid, pop, arr[i]])
            mid = temp[1]
            heapq.heappush(maxH, -temp[0])
            heapq.heappush(minH, temp[2])

            result.append(mid)

    print(result)
