# TODO 틀림 할 수 있다

m, n, l, k = map(int, input().split())
stars = []
for i in range(1, k + 1):
    r, c = map(int, input().split())
    stars.append([r, c])

result = 0
for i in range(len(stars)):
    for j in range(len(stars)):
        cnt = 0
        for cur in range(len(stars)):
            curR, curC, = stars[cur]
            if stars[i][0] <= curR <= stars[i][0] + l and \
                    stars[j][1] <= curC <= stars[j][1] + l:
                cnt += 1
        result = max(result, cnt)
print(k - result)
