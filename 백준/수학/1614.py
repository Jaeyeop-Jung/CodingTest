n = int(input())
m = int(input())

if m == 0:
    print(n - 1)
    exit()

if n == 1:
    print(8 * m)
elif n == 5:
    print(12 + (m - 1) * 8)
else:
    if m % 2 == 0:
        print(5 + (m - 1) * 4 + (n - 2))
    else:
        print(5 + (m - 1) * 4 + (5 - n - 1))