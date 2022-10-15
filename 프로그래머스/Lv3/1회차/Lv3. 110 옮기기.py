# TODO 틀림

def solution(s):
    result = []
    for i in range(len(s)):

        stack = []
        cnt = 0
        for j in range(len(s[i])):
            if ''.join(stack[-2:]) == '11' and s[i][j] == '0':
                cnt += 1
                stack.pop()
                stack.pop()
                continue
            stack.append(s[i][j])

        if cnt == 0:
            result.append(s[i])
        else:
            stack = ''.join(stack)
            rfind = stack.rfind('0')
            if rfind == -1:
                stack = '110' * cnt + stack
            else:
                stack = stack[:rfind + 1] + '110' * cnt + stack[rfind + 1:]
            result.append(stack)
    return result

print(solution(["1110","100111100","0111111010"]))