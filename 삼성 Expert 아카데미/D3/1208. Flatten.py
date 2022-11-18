
T = 10
for test_case in range(1, T + 1):
    dump = int(input())
    arr = list(map(int, input().split()))

    for i in range(dump):
        arr.sort()
        arr[0] += 1
        arr[-1] -= 1

    arr.sort()
    print('#' + str(test_case) + ' ' + str(arr[-1] - arr[0]))
