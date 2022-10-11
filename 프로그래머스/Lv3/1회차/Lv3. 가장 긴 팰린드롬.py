# TODO 틀림 메소드의 시간복잡도가 높다

def solution(s):
    length = len(s)
    if length == 1:
        return 1
    for i in range(length, 0, -1):
        for j in range(length):
            if length < j + i:
                break
            temp = s[j:j + i]
            if temp == temp[::-1]:
                return i

print(solution("abcdcba"))
print(solution("abacde"))
print(solution("wfaaaw"))
print(solution("a"))
print(solution("aa"))

