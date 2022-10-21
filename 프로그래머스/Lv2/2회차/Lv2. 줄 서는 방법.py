import math
from itertools import permutations


def solution(n, k):
    # arr = [i for i in permutations([i for i in range(1, 9)])]
    # print(arr[31230])

    boundary = 1
    for i in range(n - 1, 0, -1):
        boundary *= i

    pick = [i for i in range(1, n + 1)]
    result = []
    for i in range(n - 1, 0, -1):
        div = (k - 1) // boundary
        result.append(pick.pop(div))
        k -= div * boundary
        boundary //= i

    result += [i for i in range(1, n + 1) if i not in result]

    return result

print(solution(3, 5))