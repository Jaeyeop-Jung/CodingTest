# TODO 틀림 잘 고민해봐라 거의 다 맞았다. 다음엔 꼭 맞자. 내리지말고
























import math
import bisect
from itertools import permutations

result = math.inf
def dfs(n, start, cur, weak, dist, distIdx):
    if start + len(weak) // 2 <= cur or len(weak) <= cur:
        global result
        result = min(result, distIdx)
        return
    if len(dist) <= distIdx or result <= distIdx:
        return

    next = bisect.bisect_right(weak, weak[cur] + dist[distIdx])
    dfs(n, start, next, weak, dist, distIdx + 1)

def solution(n, weak, dist):
    dist.sort(reverse=True)
    weakSize = len(weak)
    weak.extend([i + n for i in weak])

    # 0은 dist의 idx
    for d in permutations(dist, len(dist)):
        for start in range(weakSize):
            dfs(n, start, start, weak, d, 0)
    return result if result != math.inf else -1

# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(200, [10, 25, 40, 55, 70, 90, 100, 120, 130, 150, 155, 165, 178, 190, 198], [1,2,3,4,5,6,7,8]))
print(solution(16, [1,2,3,4,5,7,8,10,11,12,14,15], [4,2,1,1]))