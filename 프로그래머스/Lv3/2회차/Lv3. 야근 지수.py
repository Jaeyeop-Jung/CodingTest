import heapq

def solution(works, n):
    h = [-w for w in works]
    heapq.heapify(h)

    for i in range(n):
        pop = heapq.heappop(h)
        pop += 1
        heapq.heappush(h, pop)

    return sum([i ** 2 for i in h if i < 0])

print(solution([4,3,3], 4))
print(solution([2,1,2], 1))
print(solution([1,1], 3))
