# from itertools import combinations
#
# T = int(input())
# for test_case in range(1, T + 1):
#     result = 0
#     n, k, = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     for i in range(1, n + 1):
#         for j in combinations(arr, i):
#             if sum(j) == k:
#                 result += 1
#
#     print('#' + str(test_case) + ' ' + str(result))

def dfs(suma, node, visited):
    if suma == k:
        global result
        result += 1
        return
    elif k < suma:
        return

    for i in range(node, n):
        if not visited[i]:
            visited[i] = True
            dfs(suma + arr[i], i, visited)
            visited[i] = False

T = int(input())
for test_case in range(1, T + 1):
    result = 0
    n, k, = map(int, input().split())
    arr = list(map(int, input().split()))

    for i in range(n):
        visited = [False] * n
        visited[i] = True
        dfs(arr[i], i, visited)
        visited[i] = False

    print('#' + str(test_case) + ' ' + str(result))