# TODO 틀림 잘 생각해봐라 이건 맞을 수 있다 

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
k = int(input())

def getRes():
    cnt = 0
    for curR in range(n):
        if curR == r:
            continue
        temp = arr[curR][:]
        for ch in change:
            temp[ch] += 1
            temp[ch] %= 2
        if all(temp):
            cnt += 1
    return cnt + 1


res = 0
for r in range(n):
    if arr[r].count(0) % 2 == k % 2 and arr[r].count(0) <= k:
        change = [i for i in range(m) if arr[r][i] == 0]
        res = max(res, getRes())

print(res)