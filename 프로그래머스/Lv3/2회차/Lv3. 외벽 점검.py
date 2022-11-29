# TODO 틀림 조금 더 고민해봐

import math

def dfs(n, weak, dist, cnt):
    if not weak:
        global result
        result = min(result, cnt)
        return
    if weak and not dist:
        return
    dist = dist[:]
    move = dist.pop()
    for i in range(len(weak)):
        start = weak[i]
        copy_week = weak[:]

        for weak_place in weak:
            if start <= weak_place <= start + move:
                copy_week.remove(weak_place)
        if n <= start + move:
            for weak_place in weak:
                if 0 <= weak_place <= (start + move) % n and weak_place in copy_week:
                    copy_week.remove(weak_place)
        dfs(n, copy_week, dist, cnt + 1)
    dist.append(move)

result = math.inf
def solution(n, weak, dist):
    dist.sort()
    dfs(n, weak, dist, 0)
    return result if result != math.inf else -1


# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# print(solution(200, [0, 100], [1,1]))
print(solution(200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]))