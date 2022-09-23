# TODO 틀림 https://hwisaek.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%98%EC%8B%9D-%EC%B5%9C%EB%8C%80%ED%99%94-Python

from itertools import permutations

def solution(expression):
    cal = ['*', '-', '+']
    stack = []
    start = 0
    for j in range(len(expression)):
        if not expression[j].isnumeric():
            stack.append(int(expression[start:j]))
            stack.append(expression[j])
            start = j + 1
    stack.append(int(expression[start:]))
    result = 0
    for i in permutations(cal):
        temp = stack[:]
        for j in list(i):
            k = 0
            while k < len(temp):
                if temp[k] == j:
                    if temp[k] == '-':
                        temp.insert(k - 1, temp[k - 1] - temp[k + 1])
                    elif temp[k] == '+':
                        temp.insert(k - 1, temp[k - 1] + temp[k + 1])
                    else:
                        temp.insert(k - 1, temp[k - 1] * temp[k + 1])
                    temp.pop(k)
                    temp.pop(k)
                    temp.pop(k)
                    continue
                k += 1
        result = max(result, abs(temp[0]))

    return result

    # def solution(expression):
    #     answer = 0
    #     num = re.split('\+|\-|\*', expression)
    #     opr = re.split('[0-9]+', expression)[1:-1]
    #     for order in permutations("+-*", 3):
    #         nc = num.copy()
    #         oc = opr.copy()
    #         for o in order:
    #             idx = 0
    #             while idx < len(oc):
    #                 if oc[idx] == o:
    #                     nc[idx] = str(eval(''.join((nc[idx], o, nc[idx + 1]))))
    #                     nc.pop(idx + 1)
    #                     oc.pop(idx)
    #                     idx -= 1
    #                 idx += 1
    #         answer = max(answer, abs(int(nc[0])))
    #     return answer

# print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
# print(solution("1"))