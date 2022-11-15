from collections import deque

def solution(s):
    result = 0
    for i in range(len(s)):
        q = deque(s)
        q.rotate(i)
        stack = []
        for gwalho in q:
            stack.append(gwalho)
            if 2 <= len(stack):
                if (stack[-1] == '}' and stack[-2] == '{') or \
                    (stack[-1] == ')' and stack[-2] == '(') or\
                    (stack[-1] == ']' and stack[-2] == '['):
                    stack.pop()
                    stack.pop()
        if not stack:
            result += 1
    return result


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)("))
print(solution("}}}"))