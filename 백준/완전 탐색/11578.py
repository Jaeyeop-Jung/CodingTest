from itertools import combinations

n, m = map(int, input().split())
arr = [list(map(int, input().split()))[1:] for _ in range(m)]

for i in range(1, m + 1):
    for case in combinations(arr, i):
        visited = [False] * (n + 1)
        for each in case:
            for num in each:
                visited[num] = True
        if visited.count(True) == len(visited) - 1:
            print(i)
            exit()



print(-1)