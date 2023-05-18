# TODO 틀림

def dfs(arr, visited, cnt):
    if m < cnt:
        global result
        result = max(result, int(''.join(arr)))
        return

    leng = len(arr)
    for i in range(leng):
        for j in range(i + 1, leng):
            arr[i], arr[j] = arr[j], arr[i]
            if int(''.join(arr)) in visited[cnt]:
                arr[i], arr[j] = arr[j], arr[i]
                continue
            visited[cnt][int(''.join(arr))] = True
            dfs(arr, visited, cnt + 1)
            arr[i], arr[j] = arr[j], arr[i]

test_case = int(input())
for t in range(1, test_case + 1):
    n, m = map(int, input().split())
    arr = list(str(n))
    result = 0
    visited = {i: {} for i in range(1, 11)}
    dfs(arr, visited, 1)
    print(f'#{t} {result}')

# 852741
# 872541