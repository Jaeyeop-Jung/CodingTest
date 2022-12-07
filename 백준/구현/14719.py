

h, w = map(int, input().split())
arr = list(map(int, input().split()))
if w == 1:
    print(0)
    exit()

result = 0
for r in range(h, -1, -1):
    left = -1
    right = -1
    for c in range(w):
        if arr[c] == r and left == -1:
            left = c
        elif arr[c] == r and right == -1:
            right = c
        if left != -1 and right != -1:
            result += right - left - 1
            left, right = right, -1

    for c in range(w):
        if r <= arr[c]:
            arr[c] = r - 1

print(result)