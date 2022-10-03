
def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def convert(n, k):
    result = ''
    while n != 0:
        q, r = divmod(n, k)
        result = str(r) + result
        n = q
    return result


def solution(n, k):
    arr = convert(n, k).split('0')
    return len([i for i in arr if i != '' and i != '1' and '0' not in i and isPrime(int(i))])

print(solution(437674, 3))
print(solution(110011, 10))
print(solution(11101, 10))
