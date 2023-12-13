from collections import deque

def solution(times, n):
    q = deque([0] * n)
    times = deque(times)
    cur = 0
    while times:
        q.rotate(-1)
        if q[0] <= cur:
            q[0] = times.popleft() + cur
        cur += 1

    q.rotate(-1)
    res = 0
    for idx, person in enumerate(q):
        res = max(res, cur + (person - cur) // n * n + idx)

    return res


# print(solution([4, 2, 1], 2))
# print(solution([8, 7, 6, 3, 4], 4))
# print(solution([13, 7, 2], 5))
# print(solution([1, 2, 3, 4, 5, 6, 7], 1))
# print(solution([1, 1, 1, 1], 5))
print(solution([1, 2, 4, 4, 4, 5], 3))