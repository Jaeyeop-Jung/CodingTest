
inp = input()

idx = 0
flag = False
while idx < len(inp):
    if flag and inp[idx] == '-':
        inp = inp[:idx] + ')' + inp[idx:]
        flag = False
    elif inp[idx] == '-':
        inp = inp[:idx + 1] + '(' + inp[idx + 1:]
        flag = True
    idx += 1
if flag:
    inp += ')'

result = ''
temp = ''
for i in inp:
    if i.isnumeric():
        temp += i
    else:
        if temp != '':
            result += str(int(temp))
            temp = ''
        result += i
if temp != '':
    result += str(int(temp))
    temp = ''

print(eval(result))