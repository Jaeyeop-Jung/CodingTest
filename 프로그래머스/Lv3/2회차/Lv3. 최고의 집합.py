
def solution(n, s):
    if s < n:
        return [-1]

    if s % n == 0:
        return [s // n] * n
    else:
        result = [s // n] * n
        backCnt = len(result) - 1
        for i in range(s % n):
            result[backCnt] += 1
            backCnt -= 1
        return result


# print(solution(2, 9))
# print(solution(2, 1))
# print(solution(2, 8))
print(solution(4, 19))