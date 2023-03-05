from collections import deque

def solution(n, m, section):
    section.sort()
    q = deque(section)

    result = 0
    while q:
        start = q.popleft()
        while q and q[0] < start + m:
            q.popleft()
        result += 1
    return result

print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))