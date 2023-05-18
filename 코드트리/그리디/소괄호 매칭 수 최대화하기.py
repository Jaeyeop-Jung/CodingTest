# TODO 틀림

n = int(input())
arr = [input() for _ in range(n)]

arr.sort(key=lambda x: (-x.count('('), x.count(')'), x))
res = list(''.join(arr))
cur = 0
result = 0
while res:
    target = res.pop()
    if target == ')':
        cur += 1
    else:
        result += cur

print(result)
