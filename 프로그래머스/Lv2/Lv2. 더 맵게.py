# TODO 틀림

import heapq

def solution(scoville, K):
    heap = scoville[:]
    heapq.heapify(heap)
    count = 0
    if heap[0] >= K:
        return 0
    for i in range(1, len(scoville)):
        popFirst = heapq.heappop(heap)
        popSecond = heapq.heappop(heap)
        if popFirst >= K:
            return i - 1
        newScovile = popFirst + (popSecond * 2)
        heapq.heappush(heap, newScovile)
        count = i

    if heapq.heappop(heap) >= K:
        return count
    return -1

i = solution([1, 1, 1], 2)
print(i)
