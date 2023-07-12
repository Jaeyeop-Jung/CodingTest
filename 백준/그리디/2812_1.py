
n, m = map(int, input().split())
arr = list(map(int, list(input())))

stack = []
cnt = 0
for i in range(n):
    while stack and stack[-1] < arr[i] and cnt != m:
        stack.pop()
        cnt += 1
    stack.append(arr[i])

for _ in range(m - cnt):
    stack.pop()

print(int(''.join(list(map(str, stack)))))