# # TODO 틀림 맞을 수 있다
#
# bracket = input()
# result = 0
# stack = []
# for i, v in enumerate(bracket):
#     if v == '(' or v == '[':
#         stack.append(v)
#     else:
#         op = 0
#         if v == ')':
#             op = 2
#         elif v == ']':
#             op = 3
#
#         rindex = -1
#         for j in range(len(stack) - 1, -1, -1):
#             if stack[j] == '(' or stack[j] == '[':
#                 if stack[j] == '(' and v == ')':
#                     rindex = j
#                     break
#                 elif stack[j] == '[' and v == ']':
#                     rindex = j
#                     break
#                 print(0)
#                 exit()
#         if rindex == -1:
#             print(0)
#             exit()
#
#         if abs(rindex - len(stack)) == 1:
#             stack.pop()
#             stack.append(op)
#         else:
#             temp = sum(stack[rindex + 1:])
#             temp *= op
#             while len(stack) != rindex:
#                 stack.pop()
#             stack.append(temp)
#
# for i in stack:
#     if type(i) == str:
#         print(0)
#         exit()
# print(sum(stack))

s = input()
stack = []
tmp = 1
res = 0

# for c in s를 하면 안 되고 길이로 돌아야 함
for i in range(len(s)):
    if s[i] == '(':
        tmp *= 2
        stack.append(s[i])
    elif s[i] == '[':
        tmp *= 3
        stack.append(s[i])

    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            res = 0
            break
        if s[i - 1] == '(':
            res += tmp
        tmp //= 2
        stack.pop()  # pop도 까먹지 말고 꼭

    else:
        if not stack or stack[-1] == '(':
            res = 0
            break
        # [()]의 경우 ] 직전 문자가 )이므로 더하지 않고 넘어감
        # 단, 이 경우는 오류는 아님
        if s[i - 1] == '[':
            res += tmp
        tmp //= 3
        stack.pop()  # pop 까먹지 말기

if stack:
    res = 0
print(res)
