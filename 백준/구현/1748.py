
n = input()
result = 0

temp = '1'
while len(temp) < len(n):
    maxi = '9' * len(temp)
    result += (int(maxi) - int(temp) + 1) * len(temp)
    temp += '0'

result += (int(n) - int(temp) + 1) * len(temp)

print(result)