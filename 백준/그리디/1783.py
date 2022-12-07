
n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(1 + (m - 1) // 2, 4))
else:
    if m <= 4:
        print(m)
    else:
        result = 1
        result += 2
        m -= 3
        flag = False
        for i in range(2):
            if 2 <= m:
                m -= 2
                result += 1
                if i == 1:
                    flag = True
        if flag:
            result += m
        print(result)