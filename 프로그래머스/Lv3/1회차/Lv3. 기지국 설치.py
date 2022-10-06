# TODO 틀림 아이디어는 맞았는데 어떻게 구현할지 고틀

import math

def solution(n, stations, w):
    result = 0

    start, end = 1, stations[0] - w
    if start < end:
        result += math.ceil((end - start) / (1 + 2 * w))
    for i in range(1, len(stations)):
        start = stations[i - 1] + w + 1
        end = stations[i] - w
        if start < end:
            result += math.ceil((end - start) / (1 + 2 * w))
    start, end = stations[-1] + w + 1, n + 1
    if start < end:
        result += math.ceil((end - start) / (1 + 2 * w))
    return result


print(solution(11, [4], 1))
print(solution(16, [9], 2))

