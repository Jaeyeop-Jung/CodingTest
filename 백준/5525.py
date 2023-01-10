# TODO 틀림 아이디어는 잘 생각했다 조금 더 집중

n = int(input())
m = int(input())
arr = list(input())

target = 'I' + 'OI' * n
result = 0
cur = ''
for i in range(len(arr)):
    if cur == '' and arr[i] == 'O':
        continue
    cur += arr[i]
    if len(cur) == len(target) and cur == target:
        result += 1
        cur = cur[2:]
    elif len(cur) == len(target):
        cur = cur[1:]
print(result)

