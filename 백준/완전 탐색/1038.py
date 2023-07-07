# TODO 틀림 이건 맞아야지;;

n = int(input())

def dfs(target, cur):
    if len(cur) == target:
        arr.append(cur)
        return

    for next in range(int(cur[-1]) - 1, -1, -1):
        dfs(target, cur + str(next))

arr = []
for i in range(9, -1, -1):
    for start in range(9, -1, -1):
        dfs(i, str(start))

arr = list(reversed(arr))
arr.append('9876543210')
if len(arr) <= n:
    print(-1)
else:
    print(arr[n])