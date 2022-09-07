
def correctBracket(inp):
    if inp == '':
        return True

    stack = [inp[0]]
    for i in range(1, len(inp)):
        stack.append(inp[i])
        if stack[-1] == ')' and stack[-2] == '(':
            stack.pop()
            stack.pop()
    if stack:
        return False
    return True

def bracket(inp):
    if inp == '':
        return ''

    # 2
    openBracketCount = 0
    closeBracketCount = 0
    idx = 0
    for i in range(len(inp) + 1):
        if openBracketCount == closeBracketCount and openBracketCount != 0:
            idx = i
            break
        if inp[i] == '(':
            openBracketCount += 1
        else:
            closeBracketCount += 1
    u = inp[:idx]
    v = inp[idx:]

    # 3
    if correctBracket(u) is True:
        return u + bracket(v)
    # 4
    else:
        temp = '(' + bracket(v) + ')'
        tempU = u[1:len(u) - 1]
        for i in tempU:
            if i == '(':
                temp += ')'
            else:
                temp += '('
        return temp


def solution(p):
    return bracket(p)


print(solution(")))((("))
