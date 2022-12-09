import sys

input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[0])

    result = 1
    award = arr[0][1]
    for i in range(1, len(arr)):
        if award < arr[i][1]:
            continue
        result += 1
        award = min(award, arr[i][1])

    print(result)