from itertools import permutations

def solution(expression):
    result = 0
    for i in permutations(['-', '+', '*']):
        stack = []
        idx = 0
        for j in range(len(expression)):
            if not expression[j].isnumeric():
                stack.append(expression[idx:j])
                stack.append(expression[j])
                idx = j + 1
        stack.append(expression[idx:])

        for j in i:
            idx = 0
            while idx < len(stack):
                if stack[idx] == j:
                    stack = stack[:idx - 1] + [str(eval(''.join(stack[idx - 1:idx + 2])))] + stack[idx + 2:]
                else:
                    idx += 1
        result = max(result, abs(int(stack[0])))
    return result


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))