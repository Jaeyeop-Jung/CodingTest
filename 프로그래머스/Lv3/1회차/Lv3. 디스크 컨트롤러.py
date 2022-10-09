import heapq

def solution(jobs):
    result = []
    cur = 0
    wait = []

    heapq.heapify(jobs)
    while jobs or wait:
        while jobs:
            if jobs[0][0] <= cur:
                p = heapq.heappop(jobs)
                heapq.heappush(wait, [p[1], p[0]])
            else:
                break
        if wait:
            p = heapq.heappop(wait)
            result.append(cur + p[0] - p[1])
            cur += p[0]
        else:
            cur += 1
    return int(sum(result) / len(result))

# print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[1, 3]]))
