# TODO 틀림 잘 생각해봐라 맞을 수 있다

n = int(input())
arr = list(map(int, input().split()))

# 테이블 만들기
dp = [[False] * n for _ in range(n)]
for start in range(n):
    stack = []
    for end in range(start, n):
        stack.append(arr[end])
        if stack[0] == stack[-1]:
            dp[start][end] = True
        else:
            break

print(dp)
# 쿼리