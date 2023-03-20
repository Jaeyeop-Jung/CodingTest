n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
for startR in range(n):
    for startC in range(m):
        for endR in range(startR, n):
            for endC in range(startC, m):
                flag = False
                cnt = 0
                for r in range(startR, endR + 1):
                    for c in range(startC, endC + 1):
                        if arr[r][c] <= 0:
                            flag = True
                            break
                        cnt += 1
                    if flag:
                        break
                else:
                    result = max(result, cnt)
print(result if result != 0 else -1)