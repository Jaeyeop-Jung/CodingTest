
def solution(lotteries):
    result = []
    for i in range(len(lotteries)):
        win, buy, price = lotteries[i]
        percent = win / (buy + 1)
        if 1 < percent:
            percent = 1
        result.append([i, percent, price])
    result.sort(key=lambda x: (x[1], x[2]))

    return result[-1][0] + 1

print(solution([[100, 100, 500], [1000, 1000, 100]]))