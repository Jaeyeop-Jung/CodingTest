
n = int(input())
stack = []
result = 0
for _ in range(n):
    x, y = map(int, input().split())
    if not stack or stack[-1] < y:
        stack.append(y)
    else:
        while stack and y < stack[-1]:
            result += 1
            stack.pop()
        if not stack and y != 0:
            stack.append(y)
        elif y != 0 and y != stack[-1]:
            stack.append(y)

print(result + len(stack) - stack.count(0))