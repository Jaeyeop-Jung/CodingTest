
n = int(input())
dp = {i ** 2: True for i in range(1, 50002)}

flag = False
for memory in range(1, 50002):
    if n + memory ** 2 in dp:
        print(int((n + memory ** 2) ** 0.5))
        flag = True
if not flag:
    print(-1)