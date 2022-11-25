# TODO 틀리진 않았는데 다시 풀어보자

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    elif len(sticker) == 2:
        return max(sticker)

    dp1 = [0] * (len(sticker) - 1)
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])
    for i in range(2, len(sticker) - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])

    sticker = [sticker.pop()] + sticker
    dp2 = [0] * (len(sticker) - 1)
    dp2[0] = sticker[0]
    dp2[1] = max(sticker[0], sticker[1])
    for i in range(2, len(sticker) - 1):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])

    return max(dp1[-1], dp2[-1])

# print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
# print(solution([1, 3, 2, 5, 4]))
print(solution([1, 2]))


