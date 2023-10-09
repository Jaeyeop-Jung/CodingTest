
def solution(s):
    res = 1
    for i in range(len(s)):
        cur = 1
        diff = 1
        while (i - diff >= 0 and len(s) > i + diff) and s[i - diff] == s[i + diff]:
            cur += 2
            diff += 1
        res = max(res, cur)

        cur = 0
        diff = 1
        while 0 <= i and i + diff < len(s) and s[i] == s[i + diff]:
            cur += 2
            diff += 2
            i -= 1
        res = max(res, cur)

    return res

print(solution("aaaa"))
