# TODO 틀림

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    elif len(sticker) == 2:
        return max(sticker[0], sticker[1])

    dp1 = [0] * len(sticker)
    dp2 = [0] * len(sticker)

    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])
    for i in range(2, len(dp1) - 1):
        dp1[i] = max(dp1[i], dp1[i - 2] + sticker[i], dp1[i - 1])

    dp2[1] = sticker[1]
    dp2[2] = max(sticker[1], sticker[2])
    for i in range(3, len(dp2)):
        dp2[i] = max(dp2[i], dp2[i - 2] + sticker[i], dp2[i - 1])
    return max(dp2 + dp1)

print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))