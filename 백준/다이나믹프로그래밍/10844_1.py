# TODO 틀림 할 수 있다 잘 생각해봐라

n = int(input())
dp = [9]
for i in range(1, n):
    dp.append((dp[-1] * 2 - i) % 1000000000)

print(dp[-1])
