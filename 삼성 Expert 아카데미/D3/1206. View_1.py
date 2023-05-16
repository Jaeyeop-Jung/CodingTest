for t in range(10):
    n = int(input())
    arr = list(map(int, input().split()))

    result = 0
    result += arr[0] - max(arr[1], arr[2]) if 0 < arr[0] - max(arr[1], arr[2]) else 0
    result += arr[1] - max(arr[0], arr[2], arr[3]) if 0 < arr[1] - max(arr[0], arr[2], arr[3]) else 0
    result += arr[-1] - max(arr[-2], arr[-3]) if 0 < arr[-1] - max(arr[-2], arr[-3]) else 0
    result += arr[-2] - max(arr[-1], arr[-3], arr[-4]) if 0 < arr[-2] - max(arr[-1], arr[-3], arr[-4]) else 0

    for i in range(2, n - 2):
        result += arr[i] - max(max(arr[i - 2:i]), max(arr[i + 1:i + 3])) if 0 < arr[i] - max(max(arr[i - 2:i]), max(arr[i + 1:i + 3])) else 0

    print(f'#{t + 1} {result}')

