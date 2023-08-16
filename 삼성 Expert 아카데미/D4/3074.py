
T = int(input())
for test_case in range(1, T + 1):
    n, m, = map(int, input().split())
    arr = [int(input()) for _ in range(n)]

    start, end = 1, max(arr) * m
    while start <= end:
        mid = (start + end) // 2
        temp = sum([mid // i for i in arr])
        if temp < m:
            start = mid + 1
        else:
            end = mid - 1

    print(f'#{test_case} {end + 1}')
