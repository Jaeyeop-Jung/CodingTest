from collections import deque


def solution(targets):
    targets.sort(key=lambda x: x[1])
    targets = deque(targets)

    result = 1
    limit = targets.popleft()[1]
    while targets:
        start, end = targets.popleft()
        if limit <= start:
            result += 1
            limit = end
    return result

print(solution([[1, 3], [2, 4], [5, 6]]))