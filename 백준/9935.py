
s = input()
destroy = input()
destroy = destroy[::-1]

result = []
for i in range(len(s) - 1, -1, -1):
    result.append(s[i])
    if len(destroy) <= len(result):
        if ''.join(result[-len(destroy):]) == destroy:
            for i in range(len(destroy)):
                result.pop()

if not result:
    print('FRULA')
    exit()
result.reverse()
print(''.join(result))