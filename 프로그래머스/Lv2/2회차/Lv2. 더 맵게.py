import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    result = 0
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        elif len(scoville) == 1 and K <= scoville[0]:
            return result

        pop1 = heapq.heappop(scoville)
        if K <= pop1:
            break
        else:
            heapq.heappush(scoville, pop1 + heapq.heappop(scoville) * 2)
            result += 1
    return result

print(solution([1, 2, 3, 9, 10, 12], 7))
