
def solution(line):
    result = ''
    stack = []
    for i in range(len(line)):
        if stack and stack[-1] != line[i]:
            if len(stack) == 1:
                result += stack[0]
            else:
                result += stack[0] + '*'
            stack.clear()
            stack.append(line[i])
        else:
            stack.append(line[i])
    if len(stack) == 1:
        result += stack[0]
    else:
        result += stack[0] + '*'


    return result

print(solution('aabbcc'))
print(solution('hellllllo'))
print(solution('wonderful'))