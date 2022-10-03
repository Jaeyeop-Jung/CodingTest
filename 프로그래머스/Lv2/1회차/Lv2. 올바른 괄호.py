from collections import deque

def solution(s):
    stack = []
    for i in s:
        if len(stack) >= 1:
            if stack[len(stack) - 1] == '(' and i == ')':
                stack.pop()
                continue
        stack.append(i)

    if stack:
        return False
    return True
