# TODO 틀림

result = []

def hanoi(n, start, mid, end):
    if n == 1:
        result.append([start, end])
        return

    hanoi(n - 1, start, end, mid)
    result.append([start, end])
    hanoi(n - 1, mid, start, end)

def solution(n):
    hanoi(n, 1, 2, 3)
    return result

print(solution(2))