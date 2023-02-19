# TODO 틀림 잘 생각해봐 조금 더 집중하면 맞출 수 있을 거 같음

def makeBin(string):
    target = 1
    l = len(string)
    while 2 ** target - 1 < l:
        target += 1
    return '0' * (2 ** target - l - 1) + string

def div(s):
    mid = len(s) // 2
    if len(s) == 0 or len(s) == 1:
        return False
    if s[mid] == '0' and not all(child == '0' for child in s):
        return True
    return div(s[:mid]) or div(s[mid + 1:])


def solution(numbers):
    result = []
    for number in numbers:
        s = bin(number)[2:]
        s = makeBin(s)
        if div(s):
            result.append(0)
        else:
            result.append(1)
    return result


print(solution([30]))
