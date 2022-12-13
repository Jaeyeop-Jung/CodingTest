# TODO 틀림 다시 잘 풀어봐

def solution(n):
    result = 0
    while 1 < n:
        if n % 2 == 0:
            n //= 2
        else:
            result += 1
            n -= 1
            n //= 2
    return result + 1


print(solution(5))
print(solution(6))
print(solution(5000))