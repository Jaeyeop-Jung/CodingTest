# TODO 틀림 맞았는데 다른 아이디어도 잘 생각해봐

dic = {
    0: [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
    1: [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
    2: [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    3: [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
    4: [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
    5: [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
    6: [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
    7: [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
    8: [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    9: [2, 4, 3, 1, 2, 1, 2, 3, 1, 0],
}

def dfs(n, k, p, x, idx, cost):
    if idx == k:
        num = int(''.join(list(map(str, x))))
        if 1 <= cost <= p and 1 <= num <= n:
            global result
            result.add(num)
            # result += 1
        return
    for j in range(len(dic[x[idx]])):
        origin = x[idx]
        x[idx] = j
        dfs(n, k, p, x, idx + 1, cost + dic[origin][j])
        x[idx] = origin


n, k, p, x, = map(int, input().split())
x = [0] * (k - len(str(x))) + list(map(int, list(str(x))))
result = set()
dfs(n, k, p, x, 0, 0)

print(len(result))