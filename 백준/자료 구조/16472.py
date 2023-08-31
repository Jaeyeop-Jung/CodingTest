
n = int(input())
s = input()

cur = {}
res = 0
for i in range(len(s)):
    cur[s[i]] = i
    temp = sorted([[key, cur[key]] for key in cur], key=lambda x: x[1])
    temp.pop()
    for _ in range(n - 1):
        if not temp:
            break
        temp.pop()
    else:
        if not temp:
            res = max(res, i + 1)
        else:
            _, idx = temp.pop()
            res = max(res, i - idx)
        continue
    res = max(res, i + 1)

print(res)
