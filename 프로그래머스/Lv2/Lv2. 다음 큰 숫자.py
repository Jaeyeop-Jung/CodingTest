from collections import Counter

def convert(num, base):
    result = ''
    while True:
        q, r = divmod(num, base)
        if q == 1:
            result = str(q) + str(r) + result
            break
        result = str(r) + result
        num = q
    return result

def solution(n):
    result = n + 1
    while True:
        if Counter(bin(n))['1'] == Counter(bin(result))['1']:
            return result
        result += 1


print(solution(78))
print(solution(15))