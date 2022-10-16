# TODO 틀림

def solution(begin, end):
    result = []
    if begin == 1:
        result.append(0)
        begin += 1

    for i in range(begin, end + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0 and i // j < 10000000:
                result.append(i // j)
                break
        else:
            result.append(1)

    return result

print(solution(1000000000 - 10, 1000000000))