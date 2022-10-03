# TODO 틀림 예외 케이스 못찾음

from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    c1 = Counter([str1[i:i + 2] for i in range(len(str1) - 1) if str1[i].isalpha() and str1[i + 1].isalpha()])
    c2 = Counter([str2[i:i + 2] for i in range(len(str2) - 1) if str2[i].isalpha() and str2[i + 1].isalpha()])
    hap = []
    for i in c1:
        if i in c2:
            for _ in range(max(c1[i], c2[i])):
                hap.append([i])
        else:
            for _ in range(c1[i]):
                hap.append([i])
    for i in c2:
        if i not in c1:
            for _ in range(c2[i]):
                hap.append([i])
    gyo = []
    for i in c1:
        if i in c2:
            for _ in range(min(c1[i], c2[i])):
                gyo.append([i])

    # 예외 처리
    if len(gyo) == 0 and len(hap) == 0:
        return 65536
    elif len(gyo) == 0 and len(hap) != 0:
        return 0

    return int(len(gyo) / len(hap) * 65536)


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('ab cd cd cd cd', 'ab ab ab ef'))