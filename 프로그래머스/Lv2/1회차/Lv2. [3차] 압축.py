from string import ascii_uppercase

def solution(msg):
    result = []
    dic = {}
    for i, j in enumerate(ascii_uppercase):
        dic[j] = i + 1

    i = 0
    flag = False
    while i != len(msg):
        temp = msg[i]
        flag = False
        for j in range(i + 1, len(msg)):
            if temp + msg[j] not in dic:
                result.append(dic[temp])
                dic[temp + msg[j]] = len(dic) + 1
                i = j
                flag = True
                break
            temp += msg[j]
        if not flag:
            result.append(dic[temp])
            break
    return result

# print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))