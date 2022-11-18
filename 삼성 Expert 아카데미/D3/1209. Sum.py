import sys
sys.stdin = open('/Users/jeongjaeyeob/Downloads/input.txt', 'r')

T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    result = max([sum(i) for i in arr])
    result = max(result, max([sum([arr[j][i] for j in range(100)]) for i in range(100)]))

    temp1 = 0
    r, c = 0, 0
    while True:
        if not 0 <= r < 100 or not 0 <= c < 100:
            break
        temp1 += arr[r][c]
        r += 1
        c += 1

    temp2 = 0
    r, c = 0, 99
    while True:
        if not 0 <= r < 100 or not 0 <= c < 100:
            break
        temp2 += arr[r][c]
        r += 1
        c -= 1

    result = max(result, temp1, temp2)

    print('#' + str(test_case) + ' ' + str(result))
