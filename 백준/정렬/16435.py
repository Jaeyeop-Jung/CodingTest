
n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))
arr.sort()

for i in range(n):
    if arr[i] <= l:
        l += 1

print(l)
