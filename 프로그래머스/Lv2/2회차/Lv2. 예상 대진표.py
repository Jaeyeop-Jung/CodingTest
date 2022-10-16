# TODO 틀림

def solution(n, a, b):
    result = 0

    while True:
        a = (a + 1) // 2
        b = (b + 1) // 2
        result += 1
        if a == b:
            return result



print(solution(8, 4, 7))