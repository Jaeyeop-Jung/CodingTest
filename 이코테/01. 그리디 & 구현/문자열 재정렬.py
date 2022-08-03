
list = list(input())

strList = []
result = 0
for i in list:
    if str(i).isnumeric():
        result += int(i)
    else:
        strList.append(str(i))

strList.sort()
print(''.join(strList) + str(result))