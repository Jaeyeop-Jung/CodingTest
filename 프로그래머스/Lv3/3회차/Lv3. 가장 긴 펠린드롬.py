

def solution(s):
    result = 1
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            if s[j:j+i] == s[j:j+i][::-1]:
                result = max(result, i)
                break
    return result

print(solution("abcdcba"))
