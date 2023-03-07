# TODO 틀림 잘 생각해봐 맞을 수 있따

import math

def check(arr, target, rowBit, columnBit):
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            cur = arr[r][c]
            if rowBit[r] == '1':
                cur ^= 1
            if columnBit[c] == '1':
                cur ^= 1
            if target[r][c] != cur:
                return False
    return True

def solution(beginning, target):
    result = math.inf
    for row in range(2 ** len(beginning)):
        for column in range(2 ** len(beginning[0])):
            rowBit = bin(row)[2:]
            columnBit = bin(column)[2:]

            cnt = rowBit.count('1') + columnBit.count('1')
            if rowBit == '1010' and columnBit == '1011':
                print()
            if cnt < result and check(beginning, target, rowBit.rjust(len(beginning), '0'), columnBit.rjust(len(beginning[0]), '0')):
                result = cnt
    return result if result != math.inf else -1


print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],[[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]))