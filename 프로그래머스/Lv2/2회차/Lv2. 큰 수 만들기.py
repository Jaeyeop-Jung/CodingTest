# TODO 틀림

def solution(number, k):

    # 앞에서 가장 큰 수 찾기
    firstNum = max(map(int, list(number[:k])))
    idx = number.index(str(firstNum))
    number = number[idx:]
    k -= idx

    stack = []
    idx = 0
    while 0 < k and idx < len(number):
        if not stack:
            stack.append(number[idx])
            idx += 1
            continue

        if int(stack[-1]) < int(number[idx]):
            stack.pop()
            k -= 1
        else:
            stack.append(number[idx])
            idx += 1

    for i in range(idx, len(number)):
        stack.append(number[i])

    stack = stack[:len(stack) - k]

    return ''.join(stack)

# print(solution('1924', 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("987654321", 2))
# print(solution("511435", 2))
