# TODO 생각보다 어렵다 하지만 할 수 있어

from string import ascii_uppercase

def upOrDown(string):
    uppercase = ascii_uppercase
    idx = uppercase.index(string)
    if len(uppercase) // 2 <= idx:
        return len(uppercase) - idx
    return idx

def getContinue(string, target):
    result = 0
    temp = 0
    flag = False
    idx = 0
    for i in range(len(string)):
        if not flag and string[i] == target:
            temp += 1
            flag = True
        elif flag and string[i] == target:
            temp += 1
        else:
            if result < temp - 1:
                result = max(result, temp)
                flag = False
                temp = 0
                idx = i - result
    result = max(result, temp)
    return idx, result

def solution(name):
    # if 'A' not in name:
    #     return sum([upOrDown(i) for i in name]) + len(name) - 1
    #
    # result = 0
    # if getContinue(name[1:len(name) // 2], 'A') < getContinue(name[len(name) // 2 + 1:], 'A'):
    #     result += len(name) - 1
    # else:
    #     if name.index('A') != 0 and name.index('A') != 1:
    #         result += (name.index('A')) * 2
    #     temp = name[name.index('A') + 1:]
    #     temp = temp[::-1]
    #     for i in range(len(temp)):
    #         if all([temp[j] == 'A' for j in range(len(temp))]):
    #             break
    #         temp = temp[1:]
    #         result += 1
    # result += sum([upOrDown(i) for i in name])
    # return result

    if 'A' not in name:
        return sum([upOrDown(i) for i in name]) + len(name) - 1
    start, cnt, = getContinue(name, 'A')
    end = start + cnt
    print(start, cnt, end)

    result = 0
    left = 0
    if start != 0 and start != 1:
        left += (start - 1) * 2
    left += len(name) - end

    right = 0
    right += (len(name) - end) * 2
    if start != 0:
        right += start - 1

    result += min(len(name) - 1, left, right)
    return result + sum([upOrDown(i) for i in name])


# print(solution('JEROEN'))
# print(solution('JAN'))
# print(solution('AAOAA'))
# print(solution('OAAJEO'))
# print(solution('AAB'))
print(solution('ABABAAAAAAABA'))