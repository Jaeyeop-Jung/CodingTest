
def solution(s):
    stack = []
    stack.append(s[0])
    index = 0
    for i in range(1, len(s)):
        if index >= 0 and stack[index] == s[i]:
            stack.pop()
            index -= 1
        else:
            stack.append(s[i])
            index += 1

        # stack.append(s[i])
        # index += 1
        # if index >= 1 and stack[index] == stack[index - 1]:
        #     stack.pop()
        #     stack.pop()
        #     index -= 2

    return not stack

solution('baabbaa')