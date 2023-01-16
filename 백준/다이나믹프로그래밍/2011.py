# TODO 틀림 잘 생각해봐 아이디어 진짜 거의 다옴

arr = list(input())
if arr[0] == '0':
    print(0)
    exit()
dp = [0] * len(arr)
if len(arr) == 1:
    print(1)
    exit()
dp[0] = 1
if 26 < int(''.join(arr[:2])):
    dp[1] = 1
else:
    dp[1] = 2
for i in range(2, len(arr)):
    # if 26 < int(''.join(arr[i - 1] + arr[i])):
    #     dp[i] = (dp[i - 1]) % 1000000
    if 0 < int(arr[i]):
        dp[i] += (dp[i - 1]) % 1000000
    if 10 <= int(''.join(arr[i - 1] + arr[i])) <= 26:
        dp[i] += (dp[i - 2] + dp[i - 1]) % 1000000

print(dp[-1])