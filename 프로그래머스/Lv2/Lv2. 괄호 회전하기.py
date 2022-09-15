
def solution(s):
    result = 0
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        stack = []
        for i in range(len(temp)):
            if len(stack) == 0 and temp[i] in [')', ']', '}']:
                stack.append(temp[i])
                break
            elif len(stack) != 0 and stack[len(stack) - 1] == '(' and temp[i] == ')':
                stack.pop()
            elif len(stack) != 0 and stack[len(stack) - 1] == '[' and temp[i] == ']':
                stack.pop()
            elif len(stack) != 0 and stack[len(stack) - 1] == '{' and temp[i] == '}':
                stack.pop()
            else:
                stack.append(temp[i])
        if not stack:
            result += 1
    return result

print(solution('[](){}'))
print(solution('}]()[{'))
print(solution('[)(]'))
print(solution('}}}'))