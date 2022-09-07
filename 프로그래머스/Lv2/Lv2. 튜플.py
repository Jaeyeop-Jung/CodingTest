def solution(s):
    result = []

    # s -> list
    # temp = []
    # valueTemp = ''
    # stack = []
    # maxValue = 0
    # for i in range(1, len(s) - 1):
    #     if len(stack) == 0 and s[i] == ',':
    #         continue
    #     if len(stack) != 0 and stack[0] == '{' and stack[len(stack) - 1] == '}':
    #         temp.append(list(stack[1:len(stack) - 1]))
    #         stack.clear()
    #         valueTemp = ''
    #         continue
    #     if s[i] == ',':
    #         stack.append(int(valueTemp))
    #         valueTemp = ''
    #         continue
    #     if s[i] == '{':
    #         stack.append(s[i])
    #         continue
    #     elif s[i] == "}":
    #         stack.append(int(valueTemp))
    #         stack.append(s[i])
    #         valueTemp = ''
    #         continue
    #     valueTemp += s[i]
    # if len(stack) != 0 and stack[0] == '{' and stack[len(stack) - 1] == '}':
    #     temp.append(list(stack[1:len(stack) - 1]))

    s1 = s.lstrip('{{').rstrip('}}').split('},{')
    s1 = [list(i.split(',')) for i in s1]
    s1.sort(key=lambda x:len(x))

    temp = s1

    # 없는거 추출
    temp.sort(key=lambda x: len(x))
    for i in range(len(temp)):
        for j in temp[i]:
            if j not in result:
                result.append(j)
                break
    return list(map(int, result))

print(solution("{{20,111},{111}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
