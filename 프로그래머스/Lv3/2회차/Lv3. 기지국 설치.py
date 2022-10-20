import math

def solution(n, stations, w):
    result = 0

    dist = []
    dist.append(stations[0] - w - 1)
    for i in range(1, len(stations)):
        dist.append(stations[i] - w - 1 - (stations[i-1] + w))
    dist.append(n - (stations[-1] + w))

    for i in dist:
        if i < 1:
            continue
        result += math.ceil(i / (2 * w + 1))

    return result


# print(solution(11, [4, 11], 1))
# print(solution(16, [9], 2))
print(solution(8, [1, 4, 6, 8], 1))
# print(solution(5, [1], 5))
# print(solution(8, [1, 8], 2))
