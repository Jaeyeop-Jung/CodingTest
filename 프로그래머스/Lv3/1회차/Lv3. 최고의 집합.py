# TODO 틀림 풀긴 풀었으나 예외를 생각해봐라

def solution(n, s):
    if s < n:
        return [-1]
    if s % n == 0:
        return [s // n] * n
    else:
        arr = [s // n] * n
        diff = s - sum(arr)
        idx = 0
        while 0 < diff:
            arr[idx] += 1
            diff -= 1
            idx += 1
            idx %= n
        return sorted(arr)


# print(solution(2, 9))
print(solution(2, 1))
# print(solution(2, 8))
print(solution(13, 100000000))
