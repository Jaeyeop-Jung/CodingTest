# TODO 틀림 https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-9251-LCS-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# https://www.youtube.com/watch?v=EAXDUxVYquY&ab_channel=Chan-SuShin

arr1 = input()
arr2 = input()

dp = [[0] * (len(arr1) + 1) for i in range(len(arr1) + 1)]
for i in range(1, len(arr1) + 1):
    for j in range(1, len(arr2) + 1):
        if arr1[i - 1] == arr2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max(map(max, dp)))