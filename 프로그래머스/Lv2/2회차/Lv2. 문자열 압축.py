import math

def solution(s):
    if len(s) == 1:
        return 1
    result = math.inf
    for i in range(1, len(s) // 2 + 1):
        tempResult = ''
        temp = s[:i]
        count = 1
        for j in range(i, len(s) + i, i):
            if len(s) <= j:
                if 1 < count:
                    tempResult += str(count) + temp
                else:
                    tempResult += temp
                break
            if temp == s[j:j + i]:
                count += 1
            elif temp != s[j:j + i] and 1 < count:
                tempResult += str(count) + temp
                temp = s[j:j + i]
                count = 1
            else:
                tempResult += temp
                temp = s[j:j + i]
                count = 1
        result = min(result, len(tempResult))
    return result

# print(solution('aabbaccc'))
# print(solution('ababcdcdababcdcd'))
# print(solution('abcabcdede'))
# print(solution('abcabcabcabcdededededede'))
# print(solution('xababcdcdababcdcd'))
print(solution('a'))
