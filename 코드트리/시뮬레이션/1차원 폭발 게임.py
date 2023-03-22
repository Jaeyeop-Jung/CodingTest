
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.reverse()
flag = True
while arr:
    cur = arr[0]
    cnt = 1
    bomb = []
    for i in range(1, len(arr)):
        if cur == arr[i]:
            cnt += 1
        else:
            if m <= cnt:
                bomb.append([i - cnt, cnt])
            cnt = 1
            cur = arr[i]
    if m <= cnt:
        bomb.append([len(arr) - 1 - cnt + 1, cnt])
    if not bomb:
        break

    bomb.reverse()
    for start, cnt in bomb:
        for _ in range(cnt):
            arr.pop(start)

print(len(arr))
arr.reverse()
for i in arr:
    print(i)
