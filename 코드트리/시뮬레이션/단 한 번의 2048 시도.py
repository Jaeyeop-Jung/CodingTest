
arr = [list(map(int, input().split())) for _ in range(4)]
d = input()

if d == 'R':
    for r in range(4):
        temp = [0] * 4
        idx = 3
        for c in range(3, -1, -1):
            if arr[r][c] != 0:
                temp[idx] = arr[r][c]
                idx -= 1

        i = 3
        idx = 3
        while 0 <= i:
            if 1 <= i and temp[i - 1] == temp[i]:
                temp[idx] = temp[i] * 2
                i -= 1
            else:
                temp[idx] = temp[i]
            i -= 1
            idx -= 1
        while 0 <= idx:
            temp[idx] = 0
            idx -= 1
        arr[r] = temp
elif d == 'L':
    for r in range(4):
        temp = [0] * 4
        idx = 0
        for c in range(4):
            if arr[r][c] != 0:
                temp[idx] = arr[r][c]
                idx += 1

        i = 0
        idx = 0
        while i < 4:
            if i < 3 and temp[i + 1] == temp[i]:
                temp[idx] = temp[i] * 2
                i += 1
            else:
                temp[idx] = temp[i]
            i += 1
            idx += 1
        while idx < 4:
            temp[idx] = 0
            idx += 1
        arr[r] = temp
elif d == 'D':
    for c in range(4):
        temp = [0] * 4
        idx = 3
        for r in range(3, -1, -1):
            if arr[r][c] != 0:
                temp[idx] = arr[r][c]
                idx -= 1

        i = 3
        idx = 3
        while 0 <= i:
            if 1 <= i and temp[i - 1] == temp[i]:
                temp[idx] = temp[i] * 2
                i -= 1
            else:
                temp[idx] = temp[i]
            i -= 1
            idx -= 1
        while 0 <= idx:
            temp[idx] = 0
            idx -= 1
        for r in range(4):
            arr[r][c] = temp[r]
else:
    for c in range(4):
        temp = [0] * 4
        idx = 0
        for r in range(4):
            if arr[r][c] != 0:
                temp[idx] = arr[r][c]
                idx += 1

        i = 0
        idx = 0
        while i < 4:
            if i < 3 and temp[i + 1] == temp[i]:
                temp[idx] = temp[i] * 2
                i += 1
            else:
                temp[idx] = temp[i]
            i += 1
            idx += 1
        while idx < 4:
            temp[idx] = 0
            idx += 1
        for r in range(4):
            arr[r][c] = temp[r]

for i in arr:
    print(*i)