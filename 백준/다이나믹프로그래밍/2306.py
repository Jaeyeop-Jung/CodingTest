# TODO 틀림

s = input()

def getKOI(s):
    cnt = 0
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        elif s[i] == 't':
            if stack[-1] != 'a':
                break
            stack.pop()
            cnt += 1
        elif s[i] == 'c':
            if stack[-1] != 'g':
                break
            stack.pop()
            cnt += 1
        else:
            stack.append(s[i])
    else:
        return cnt * 2
    return 0

def dfs(dp, cur, idx):
    if len(s) <= idx:
        return
    if dp[idx] <= getKOI(cur + s[idx]):
        dp[idx] = getKOI(cur + s[idx])
        dfs(dp, cur + s[idx], idx + 1)
    if dp[idx] <= getKOI(cur):
        dp[idx] = getKOI(cur)
        dfs(dp, cur, idx + 1)

dp = [0] * len(s)
dfs(dp, '', 0)
print(max(dp))