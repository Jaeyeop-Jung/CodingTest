# TODO 틀림 아이디어를 더 생각해봐 할 수 있어

import math

def solution(a):
    leftMin = [math.inf] * len(a)
    rightMin = [math.inf] * len(a)
    temp = math.inf
    for i in range(len(a)):
        temp = min(temp, a[i])
        leftMin[i] = temp
    temp = math.inf
    for i in range(len(a) - 1, -1, -1):
        temp = min(temp, a[i])
        rightMin[i] = temp

    result = 0
    for i in range(len(a)):
        if leftMin[i] < a[i] and rightMin[i] < a[i]:
            continue
        result += 1

    return result

# print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
