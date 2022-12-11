
s = input()

oneRes = 0
zeroRes = 0
oneFlag = False
for i in range(len(s)):
    if oneFlag and s[i] == '0':
        oneFlag = False
        oneRes += 1
    elif s[i] == '1':
        oneFlag = True
if oneFlag:
    oneRes += 1

zeroFlag = False
for i in range(len(s)):
    if zeroFlag and s[i] == '1':
        zeroFlag = False
        zeroRes += 1
    elif s[i] == '0':
        zeroFlag = True
if zeroFlag:
    zeroRes += 1

print(min(oneRes, zeroRes))