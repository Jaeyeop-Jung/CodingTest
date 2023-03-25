# TODO 틀림 다음엔 맞출 수 있다

import math

def isAvailable(binary, start, end, parent):
    if start == end:
        if parent and binary[start] == '1':
            return False
        return True
    mid = (start + end) // 2
    if parent and binary[mid] == '1':
        return False
    if binary[mid] == '0':
        return isAvailable(binary, start, mid - 1, True) and isAvailable(binary, mid + 1, end, True)
    else:
        return isAvailable(binary, start, mid - 1, parent) and isAvailable(binary, mid + 1, end, parent)

def solution(numbers):
    result = []
    for number in numbers:
        binary = bin(number)[2:]
        total = 2 ** int(math.log2(len(binary)) + 1) - 1
        binary = '0' * (total - len(binary)) + binary
        if isAvailable(binary, 0, len(binary) - 1, False):
            result.append(1)
        else:
            result.append(0)
    return result

print(solution([7, 42, 5]))
