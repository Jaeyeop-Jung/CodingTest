
def solution(prices, k):
    res = 0
    for i in range(len(prices)):
        cur = prices[i]
        temp = sorted(prices[i + 1:])
        cnt = 0
        if len(temp) < k:
            continue
        for _ in range(k):
            cnt += temp.pop() - cur
        res = max(res, cnt)
    return res if res != 0 else -1

print(solution([10, 7, 8, 5, 8, 7, 6, 2, 9], 3))
