# TODO 틀림 아이디어를 잘 생각

n = input()
if '0' not in n:
    print(-1)
    exit()

if sum(map(int, n.split())) % 3 != 0:
    print(-1)
    exit()

print(int(''.join(sorted(n, reverse=True))))



