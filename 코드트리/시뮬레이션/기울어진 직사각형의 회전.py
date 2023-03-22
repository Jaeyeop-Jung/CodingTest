
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, d = map(int, input().split())
r, c = r - 1, c - 1

if d == 0:
    dR = [-1, -1, 1, 1]
    dC = [1, -1, -1, 1]
    movement = [m1, m2, m3, m4]
else:
    dR = [-1, -1, 1, 1]
    dC = [-1, 1, 1, -1]
    movement = [m4, m3, m2, m1]

temp = arr[r][c]
for i in range(4):
    for _ in range(movement[i]):
        movedR, movedC = r + dR[i], c + dC[i]
        temp2 = arr[movedR][movedC]
        arr[movedR][movedC] = temp
        temp = temp2
        r, c = movedR, movedC

for i in arr:
    print(*i)