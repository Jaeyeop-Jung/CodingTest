import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [input().strip() for _ in range(n)]
    arr.sort()

    dic = {}
    flag = False
    for i in range(n):
        cur = arr[i][0]
        if cur in dic:
            flag = True
            break
        for j in range(1, len(arr[i])):
            cur += arr[i][j]
            if cur in dic:
                flag = True
                break
        if flag:
            break
        dic[cur] = 1
    if flag:
        print('NO')
    else:
        print('YES')