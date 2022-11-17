# TODO 틀림

from itertools import combinations

def dfs(arr, cnt):
    global visited
    if cnt == change:
        global result
        result = max(result, int(''.join(arr)))
        return

    for i in combinations([i for i in range(len(arr))], 2):
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
        if (''.join(arr), cnt+1) not in visited:
            dfs(arr, cnt + 1)
            visited.add((''.join(arr), cnt+1))
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]]
    # for ci in range(len(arr)):
    #     for cj in range(len(arr)):
    #         if ci != cj:
    #             arr[ci], arr[cj] = arr[cj], arr[ci]
    #             dfs(arr, cnt + 1)
    #             arr[ci], arr[cj] = arr[cj], arr[ci]

T = int(input())
result = 0
for test_case in range(1, T + 1):
    arr, change = input().split(' ')
    arr = list(arr)
    change = int(change)

    visited = set()
    dfs(arr, 0)

    print('#' + str(test_case) + ' ' + str(result))
    result = 0