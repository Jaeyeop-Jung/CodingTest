from collections import deque

def solution(priorities, location):
    q = deque([[index, priority] for index, priority in enumerate(priorities)])
    result = []
    maxPriority = max(priorities)
    while q:
        pop = q.popleft()
        if pop[1] == maxPriority:
            result.append(pop)
            if q:
                maxPriority = max([i[1] for i in q])
        else:
            q.append(pop)
    return result.index([location, priorities[location]]) + 1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))