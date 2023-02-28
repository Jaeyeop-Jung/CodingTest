
def dfs(cur, n, route):
    if n < cur:
        temp = ''.join(route.split(' '))
        if eval(temp) == 0:
            global result
            result.append(route)
        return

    dfs(cur + 1, n, route + '+' + str(cur))
    dfs(cur + 1, n, route + '-' + str(cur))
    dfs(cur + 1, n, route + ' ' + str(cur))

t = int(input())
for _ in range(t):
    n = int(input())
    result = []
    dfs(2, n, '1')
    result.sort()
    for i in result:
        print(i)
    print()