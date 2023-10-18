
t = int(input())
for _ in range(t):
    n = int(input())
    num = list(map(int, list(input())))
    arr = list(input())

    idx = 0
    while idx < n:
        if arr[idx] == '*':
            idx += 1
            continue
        cnt = arr[max(0, idx - 1):min(idx + 2, n)].count('*')
        if cnt < num[idx]:
            if 0 < idx:
                pre = arr[max(0, idx - 2):min(idx + 1, n)].count('*')
                if num[idx - 1] < pre + 1:
                    idx += 1
                    continue
            arr[idx] = '*'
        idx += 1

    print(arr.count('*'))