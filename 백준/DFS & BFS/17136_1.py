# TODO 틀림 니가 생각한거에 반례가 없나 깊게 생각해봐라

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

cnt = [5, 5, 5, 5, 5]
arr = [list(map(int, input().split())) for _ in range(10)]
for r in range(10):
    for c in range(10):
        if arr[r][c]:
            total = []
            for i in range(1, 6):
                temp = []
                move = i - 1
                sR, sC = r + dR[0] * move, c + dC[0] * move
                if not arr[sR][sC]:
                    break
                temp.append((sR, sC))

                # 밑에 탐색
                flag = False
                for _ in range(move):
                    movedR, movedC = sR + dR[1], sC + dC[1]
                    if not 0 <= movedR < 10 or not 0 <= movedC < 10:
                        flag = True
                        break
                    if not arr[movedR][movedC]:
                        flag = True
                        break
                    temp.append((movedR, movedC))
                    sR, sC = movedR, movedC
                else: # 왼쪽 탐색
                    for _ in range(move):
                        movedR, movedC = sR + dR[2], sC + dC[2]
                        if not 0 <= movedR < 10 or not 0 <= movedC < 10:
                            flag = True
                            break
                        if not arr[movedR][movedC]:
                            flag = True
                            break
                        temp.append((movedR, movedC))
                        sR, sC = movedR, movedC
                    else:
                        total += temp
                if flag:
                    break

            for i in range(i - 1, 0, -1):
                if not cnt[i - 1]:
                    for _ in range(i * 2 - 1):
                        total.pop()
                else:
                    for eR, eC in total:
                        arr[eR][eC] = 0
                    cnt[i - 1] -= 1
                    break

if sum(map(sum, arr)):
    print(-1)
else:
    print(25 - sum(cnt))