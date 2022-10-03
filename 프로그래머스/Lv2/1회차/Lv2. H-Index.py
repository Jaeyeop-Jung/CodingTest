from bisect import bisect_left

def solution(citations):
    citations.sort()
    total = len(citations)
    if total == 1:
        return citations[0]

    result = 0
    for i in range(max(citations)):
        if i <= total - bisect_left(citations, i):
            result = max(result, i)
    return result

print(solution([3, 0, 6, 1, 5]))
print(solution([1]))