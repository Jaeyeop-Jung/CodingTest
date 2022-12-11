# TODO 틀림 잘 생각해라 맞을 수 있어


def solution(k, d):
    result = 0
    for a in range(d // k + 1):
        for b in range(d // k + 1):
            if (k * a) ** 2 + (k * b) ** 2 <= d ** 2:
                result += 1
    return result



print(solution(2, 4))
print(solution(1, 5))