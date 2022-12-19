
while True:
    message = input()
    if message == '.':
        break

    stack = []
    for m in message:
        if m == '[' or m == '(':
            stack.append(m)
        elif m == ']':
            if not stack:
                print('no')
                break
            elif stack and stack[-1] != '[':
                print('no')
                break
            stack.pop()
        elif m == ')':
            if not stack:
                print('no')
                break
            elif stack and stack[-1] != '(':
                print('no')
                break
            stack.pop()
    else:
        if not stack:
            print('yes')
        else:
            print('no')