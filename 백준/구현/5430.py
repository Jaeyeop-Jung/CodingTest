
t = int(input())
for _ in range(t):
    cmd = input()
    n = int(input())
    arr = input()
    if arr == '[]':
        arr = []
    else:
        arr = list(map(int, arr[1:-1].split(',')))

    if n < cmd.count('D'):
        print('error')
        continue

    flag = False
    for c in cmd:
        if c == 'R':
            flag ^= True
        elif c == 'D':
            if flag:
                arr.pop()
            else:
                arr.pop(0)

    if flag:
        arr.reverse()
    print('[' + ','.join(map(str, arr)) + ']')
