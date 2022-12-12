import math


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    arr1 = [str1[i:i+2] for i in range(len(str1) - 1) if str1[i:i+2].isalpha()]
    arr2 = [str2[i:i+2] for i in range(len(str2) - 1) if str2[i:i+2].isalpha()]

    gyo = 0
    gyo_set = set()
    for i in arr1:
        if i in arr2 and i not in gyo_set:
            gyo += min(arr2.count(i), arr1.count(i))
            gyo_set.add(i)

    hap = 0
    hap_set = set()
    for i in arr1:
        if i not in hap_set:
            hap += max(arr1.count(i), arr2.count(i))
            hap_set.add(i)
    for i in arr2:
        if i not in hap_set:
            hap += max(arr1.count(i), arr2.count(i))
            hap_set.add(i)

    if hap == 0:
        return 1 * 65536
    return math.trunc((gyo / hap) * 65536)

print(solution('FRANCE', 'french'))
print(solution('aa1+aa2', 'AAAA12'))
