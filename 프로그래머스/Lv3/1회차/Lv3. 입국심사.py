

def solution(n, times):
    start = 0
    end = max(times) * n
    while start <= end:
        mid = (start + end) // 2
        passed = sum([mid // i for i in times])
        if passed < n:
            start = mid + 1
        else:
            end = mid - 1
    return start
print(solution(6, [7, 10]))
