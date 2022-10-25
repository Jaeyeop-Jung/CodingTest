
T = int(input())
result = []

for test_case in range(1, T + 1):
    word = input()
    stack = []
    for i in range(len(word)):
        if not stack:
            stack.append(word[i])
        else:
            if word[i] in stack:
                stack.pop(stack.index(word[i]))
            else:
                stack.append(word[i])

    if not stack:
        result.append('#' + str(test_case) + ' ' + 'Good')
    else:
        result.append('#' + str(test_case) + ' ' + ''.join(sorted(stack)))

for i in result:
    print(i)