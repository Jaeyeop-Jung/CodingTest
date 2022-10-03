from math import gcd

def lcm(a, b):
    return gcd(a, b) * a // gcd(a, b) * b // gcd(a, b)

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return lcm(arr[0], arr[1])
    else:
        result = lcm(arr[0], arr[1])
        for i in range(2, len(arr)):
            result = lcm(result, arr[i])
        return result


print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))