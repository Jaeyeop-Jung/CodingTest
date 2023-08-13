
s = input()
stack = []
cnt = 0
idx = len(s) - 1
while 0 <= idx:
    if s[idx] == ')':
        stack.append(')')
    elif s[idx] == '(':
        tempCnt = 0
        while stack:
            if stack[-1].isnumeric():
                tempCnt += int(stack.pop())
            else:
                break
        idx -= 1
        stack.pop()
        stack.append(str(int(s[idx]) * int(tempCnt)))
    else:
        stack.append('1')
    idx -= 1

print(sum(map(int, stack)))
