# TODO 틀림 아이디어는 맞았으나 구현을 다시

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = [str1[i:i+2] for i in range(len(str1) - 1) if str1[i].isalpha() and str1[i + 1].isalpha()]
    arr2 = [str2[i:i+2] for i in range(len(str2) - 1) if str2[i].isalpha() and str2[i + 1].isalpha()]

    gyo = 0
    for i in set(arr1):
        if i in arr2:
            gyo += min(arr1.count(i), arr2.count(i))

    hap = 0
    for i in set(arr1):
        if i in arr2:
            hap += max(arr1.count(i), arr2.count(i))
        else:
            hap += arr1.count(i)
    for i in set(arr2):
        if i not in arr1:
            hap += arr2.count(i)

    if hap == 0:
        return 1 * 65536
    # return int(gyo / (len(arr1) + len(arr2) - gyo) * 65536)
    return int(gyo / hap * 65536)

# print(solution('FRANCE', 'french'))
# print(solution('handshake', 'shake hands'))
# print(solution('aa1+aa2', 'AAAA12'))
# print(solution('E=M*C^2', 'e=m*c^2'))
# print(solution('FRANCE', 'french'))
print(solution("AAAA+BBBB", "aa+aa+bb+bb"))