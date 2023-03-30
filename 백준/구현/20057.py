
dR = [0, 1, 0, -1]
dC = [-1, 0, 1, 0]

expand = [
    [
        [-1, 0, 7], [-2, 0, 2], [-1, -1, 10], [-1, 1, 1], [1, 0, 7], [2, 0, 2], [1, -1, 10], [1, 1, 1], [0, -2, 5]
    ],
    [
        [-1, -1, 1], [0, -1, 7], [0, -2, 2], [1, -1, 10], [-1, 1, 1], [0, 1, 7], [0, 2, 2], [1, 1, 10], [2, 0, 5]
    ]
    ,
    [
        [-1, 0, 7], [-2, 0, 2], [-1, -1, 1], [-1, 1, 10], [1, 0, 7], [2, 0, 2], [1, -1, 1], [1, 1, 10], [0, 2, 5]
    ],
    [
        [1, -1, 1], [0, -1, 7], [0, -2, 2], [-1, -1, 10], [1, 1, 1], [0, 1, 7], [0, 2, 2], [-1, 1, 10], [-2, 0, 5]
    ]
]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

r, c, = n // 2, n // 2
moveCnt = 1
direction = 0
moveFlag = 0
isEnd = True
result = 0
while isEnd:
    for _ in range(moveCnt):
        if r == 0 and c == 0:
            isEnd = False
            break
        movedR, movedC = r + dR[direction], c + dC[direction]
        dustTemp = arr[movedR][movedC]
        dust = dustTemp
        for expandR, expandC, per in expand[direction]:
            nextR, nextC = movedR + expandR, movedC + expandC
            if not 0 <= nextR < n or not 0 <= nextC < n:
                result += int(dust * (per / 100))
            else:
                arr[nextR][nextC] += int(dust * (per / 100))
            dustTemp -= int(dust * (per / 100))

        alphaR, alphaC = movedR + dR[direction], movedC + dC[direction]
        if not 0 <= alphaR < n or not 0 <= alphaC < n:
            result += dustTemp
        else:
            arr[alphaR][alphaC] += dustTemp

        r, c = movedR, movedC

    direction += 1
    direction %= 4
    moveFlag += 1
    if moveFlag == 2:
        moveCnt += 1
        moveFlag = 0

print(result)
