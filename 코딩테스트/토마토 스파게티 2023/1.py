
def solution(s, N):
    res = -1
    for start in range(len(s)):
        temp = ''
        for i in range(start, min(len(s), start + N)):
            temp += s[i]
        for i in range(1, len(temp) + 1):
            if str(i) not in temp:
                break
        else:
            res = max(res, int(temp))

    return res

# print(solution("1451232125", 2))
print(solution("313253123", 3))