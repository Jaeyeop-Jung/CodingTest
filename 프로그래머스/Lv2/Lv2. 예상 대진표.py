# TODO 틀림 https://velog.io/@radm90/Programmers-Lv.2-%EC%98%88%EC%83%81-%EB%8C%80%EC%A7%84%ED%91%9C

from math import log

def solution(n, a, b):
    result = int(log(n, 2))
    mid = int(n / 2)
    left = 0
    right = n
    while True:
        if a <= mid < b or b <= mid < a:
            break
        elif a <= b <= mid or b <= a <= mid:
            right = mid
            mid = (left + right) // 2
        elif mid <= a <= b or mid <= b <= a:
            left = mid
            mid = (left + right) // 2
        result -= 1

    return result


print(solution(16, 12, 13))