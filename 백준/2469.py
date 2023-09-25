from string import ascii_uppercase

k = int(input())
n = int(input())
target = list(input())
arr = [list(input()) for _ in range(n)]

top = list(ascii_uppercase[:k])
for r in range(n):
    if arr[r][0] == '?':
        break
    for c in range(k - 1):
        if arr[r][c] == '-':
            top[c], top[c + 1] = top[c + 1], top[c]

bottom = target
for r in range(n - 1, -1, -1):
    if arr[r][0] == '?':
        break
    for c in range(k - 1):
        if arr[r][c] == '-':
            bottom[c], bottom[c + 1] = bottom[c + 1], bottom[c]

for sC in range(k):
    for eC in range(k):
        if top[sC] == bottom[eC]:
            if 2 <= abs(sC - eC):
                print('x' * (k - 1))
                exit()
            break

res = []
for c in range(k - 1):
    if top[c] == bottom[c + 1] and top[c + 1] == bottom[c]:
        res.append('-')
    else:
        res.append('*')

# cur = target
# for emptyR in range(n):
#     if arr[emptyR][0] == '?':
#         arr[emptyR] = res
#         for r in range(n - 1, -1, -1):
#             for c in range(k - 1):
#                 if arr[r][c] == '-':
#                     cur[c], cur[c + 1] = cur[c + 1], cur[c]


# if list(ascii_uppercase[:k]) == cur:
#     print(''.join(res))
# else:
#     print('x' * k)

print(''.join(res))