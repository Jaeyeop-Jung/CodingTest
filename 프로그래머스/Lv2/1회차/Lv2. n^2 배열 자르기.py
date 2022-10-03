
def solution(n, left, right):
    result = []
    for i in range(left, right + 1):
        q = i // n
        r = i % n
        result.append(max(q, r) + 1)
    return result


print(solution(3, 2, 5))
print(solution(4, 7, 14))