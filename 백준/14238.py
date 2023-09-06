from collections import Counter

target = input()
dic = dict(Counter(target))
arr = [''] * len(target)

idx = 0
for i in range(dic['C']):
    if len(arr) <= idx:
        print(-1)
        exit()
    arr[idx] = 'C'
    idx += 3

idx = 1
for i in range(dic['B']):
    if len(arr) <= idx:
        print(-1)
        exit()
    while arr[idx] != '':
        idx += 1
        if len(arr) <= idx:
            print(-1)
            exit()
    arr[idx] = 'B'
    idx += 2

for i in range(len(arr)):
    if arr[i] == '':
        arr[i] = 'A'

print(''.join(arr))
