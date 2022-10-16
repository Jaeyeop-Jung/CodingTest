# TODO 틀림

def solution(prices):
    length = len(prices)
    result = [length - 1 -i for i in range(length)]
    result[-1] = 0
    prices = [[i, value] for i, value in enumerate(prices)]

    stack = [prices[0]]
    for i in range(1, length):
        while True:
            if stack and prices[i][1] < stack[-1][1]:
                idx, _ = stack.pop()
                result[idx] = i - idx
            else:
                stack.append(prices[i])
                break

    return result


print(solution([1, 2, 3, 2, 3]))
print(solution([3, 2, 1]))