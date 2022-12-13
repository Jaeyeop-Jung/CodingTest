
def solution(begin, end):
    result = []
    for i in range(begin, end + 1):
        if i == 1:
            result.append(0)
            continue
        elif i == 2 or i == 3:
            result.append(1)
            continue

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                if 10000000 < i // j:
                    continue
                result.append(i // j)
                break
        else:
            result.append(1)
    return result



print(solution(1, 10))