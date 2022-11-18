

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input())))

    involve = 1
    r = 0
    result = 0
    while involve <= n:
        result += sum(arr[r][n // 2 - involve // 2:n // 2 + involve // 2 + 1])
        involve += 2
        r += 1
    involve -= 2
    while r < n:
        involve -= 2
        result += sum(arr[r][n // 2 - involve // 2:n // 2 + involve // 2 + 1])
        r += 1

    print('#' + str(test_case) + ' ' + str(result))