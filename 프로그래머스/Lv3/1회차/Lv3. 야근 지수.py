# TODO 틀림 자료구조를 잘 골라보자

import heapq

def solution(n, works):
    works = [-i for i in works]
    heapq.heapify(works)

    for i in range(n):
        heapq.heappush(works, heapq.heappop(works) + 1)

    return sum([i ** 2 for i in works if not 1 <= i])

print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))