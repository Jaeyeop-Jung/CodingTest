
s = input()
res = ''

i = 0
cnt = 0
while i < len(s):
    if i + 1 < len(s) and s[i] == ':' and s[i + 1] == ':':
        res += '::'
        i += 2
    elif s[i] == ':':
        res += ':'
        i += 1
    else:
        temp = ''
        cur = i
        while cur < len(s) and s[cur] != ':':
            temp += s[cur]
            cur += 1
        temp = temp.rjust(4, '0')
        res += temp
        i = cur
        cnt += 1

if '::' in res:
    if res.startswith('::'):
        res = res[2:]
        res = '0000:' * (8 - cnt) + res
    elif res.endswith('::'):
        res = res[:-2]
        res += ':0000' * (8 - cnt)
    else:
        idx = res.index('::')
        res = res[:idx] + res[idx + 2:]
        res = res[:idx] + ':' + '0000:' * (8 - cnt) + res[idx:]

print(res)