
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = 1

    multiple = 1
    dvided = 1
    for i in range(m, m - n, -1):
        multiple *= i
    for i in range(n, 0, -1):
        dvided *= i

    print(int(multiple / dvided))