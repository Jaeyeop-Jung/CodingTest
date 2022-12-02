# TODO 틀림 잘 생각해봐 풀 수 있어

def solution(s):
    result = []
    for each in s:
        stack = []
        cnt = 0
        for i in range(len(each)):
            stack.append(each[i])
            if len(stack) < 3:
                continue
            if stack[-3] == '1' and stack[-2] == '1' and stack[-1] == '0':
                cnt += 1
                del stack[-3:]

        temp = ''.join(stack)
        if '0' in temp:
            idx = temp.rindex('0')
            temp = temp[:idx + 1] + '110' * cnt + temp[idx + 1:]
        else:
            temp = '110' * cnt + temp
        result.append(temp)

    return result


print(solution(["1110", "100111100", "0111111010"]))
