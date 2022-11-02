
def solution(s):
    result = 1
    flag = False
    for i in range(len(s), 0, -1):
        for j in range(len(s)):
            if len(s) < j + i:
                break
            temp = s[j:j + i]
            mid = len(temp) // 2
            if i % 2 == 0:
                tempRes = 0
                cnt = 0
                while 0 <= mid - 1 - cnt and mid + cnt < len(temp):
                    if temp[mid - 1 - cnt] == temp[mid + cnt]:
                        tempRes += 2
                        cnt += 1
                    else:
                        break
                else:
                    flag = True
                result = max(result, tempRes)
            else:
                tempRes = 1
                cnt = 1
                while 0 <= mid - cnt and mid + cnt < len(temp):
                    if temp[mid - cnt] == temp[mid + cnt]:
                        tempRes += 2
                        cnt += 1
                    else:
                        break
                else:
                    flag = True
                result = max(result, tempRes)
            if flag:
                return result

    return result

# print(solution("abcdcba"))
# print(solution("abacde"))
# print(solution("aa"))
print(solution("aaaa"))