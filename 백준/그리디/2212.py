# TODO 틀림 맞았는데 왜인지 증명을 못함

n = int(input())
k = int(input())
arr = list(map(int, input().split()))

arr.sort()
term = []
for i in range(n - 1):
    term.append(arr[i + 1] - arr[i])
term.sort()
for _ in range(k - 1):
    if term:
        term.pop()

print(sum(term))
