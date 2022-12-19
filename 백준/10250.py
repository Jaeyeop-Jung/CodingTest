
t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    height = n % h
    if height == 0:
        height = h
    if n % h == 0:
        width = n // h
    else:
        width = n // h + 1
    # if h == 1:
    # width = n // h
    print(str(height) + str(width).rjust(2, '0'))
