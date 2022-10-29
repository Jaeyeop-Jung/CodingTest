
def solution(distance, scope, times):
    for i, v in enumerate(scope):
        for j in range(min(v), max(v) + 1):
            cycle = sum(times[i])
            if 0 < j % cycle <= times[i][0]:
                distance = min(distance, j)
    return distance

print(solution(10, [[3, 4], [5, 8]], [[2, 5], [4, 3]]))
print(solution(12, [[7, 8], [4, 6], [11, 10]], [[2, 2], [2, 4], [3, 3]]))