
T = int(input())
for test_case in range(1, T + 1):
    result = 0
    arr = list(map(int, input().split()))
    for i in arr:
        if i % 2 == 1:
            result += i
    print('#' + str(test_case) + ' ' + str(result))
