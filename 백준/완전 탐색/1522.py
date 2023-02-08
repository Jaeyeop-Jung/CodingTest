# TODO 틀림 이건 맞아야지.. 잘 생각해봐 할 수 있다

import math

s = input()
total = s.count('a')
result = math.inf
for i in range(len(s)):
    cnt = 0
    for j in range(i, i + total):
        j %= len(s)
        if s[j] != 'a':
            cnt += 1
    result = min(result, cnt)

print(result)
