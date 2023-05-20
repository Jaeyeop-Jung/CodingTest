
n = int(input())
cur = list(map(int, list(input())))
target = list(map(int, list(input())))

def simul(cur):
    cnt = 0
    for i in range(1, n - 1):
        if cur[i - 1] == target[i - 1]:
            continue
        cur[i - 1] ^= 1
        cur[i] ^= 1
        cur[i + 1] ^= 1
        cnt += 1

    if cur[-2] != target[-2]:
        cur[-2] ^= 1
        cur[-1] ^= 1
        cnt += 1

    return cur == target, cnt


res, cnt = simul(cur[:])
if res:
    print(cnt)
    exit()

cur[0] ^= 1
cur[1] ^= 1
res, cnt = simul(cur)
if res:
    print(cnt + 1)
    exit()

print(-1)
