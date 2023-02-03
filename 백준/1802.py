# TODO 틀림

def check(s):
    if s == '':
        return False
    mid = len(s) // 2
    for i in range(mid):
        if s[i] == s[len(s) - 1 - i]:
            return True
    return check(s[:mid]) or check(s[mid + 1:])


t = int(input())
for _ in range(t):
    s = input()
    if check(s):
        print('NO')
    else:
        print('YES')
