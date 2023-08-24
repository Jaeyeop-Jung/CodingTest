import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    res = []
    cur = int(input())
    cnt = [0, 0, 0, 0, 0]

    # 60으로 다 처리하고
    cnt[0] += cur // 60
    cur %= 60
    # 60을 만들어서 빼자
    addOne = cnt[:]
    minusOne = cnt[:]
        # 1로 10단위로 만들어서
            # 1을 더해서
    addOne[-2] += 10 - (cur % 10)
            # 1을 빼서
    minusOne[-1] += cur % 10
        # 10단위를 더하고
    addOne[1] += (6 - (cur + 10) // 10)
    minusOne[1] += (6 - cur // 10)
        # 해본다
    addOne[0] += 1
    minusOne[0] += 1
    res.append(addOne)
    res.append(minusOne)


    # 10단위로 만들어서 빼자
    addOne = cnt[:]
    minusOne = cnt[:]
    # 1로 10단위로 만들어서
    # 1을 더해서
    addOne[-2] += 10 - (cur % 10)
    copy = (cur + 10) - cur % 10
    addOne[2] += copy // 10
    res.append(addOne)
    # 1을 빼서
    minusOne[-1] += cur % 10
    copy = cur - cur % 10
    minusOne[2] += copy // 10
    res.append(minusOne)

    for i in range(len(res)):
        temp = res[i]
        res[i] = [temp[0], temp[2], temp[1], temp[4], temp[3]]

    res.sort(key=lambda x: (sum(x), x[0], x[1], x[2], x[3], x[4]))
    print(*res[0])