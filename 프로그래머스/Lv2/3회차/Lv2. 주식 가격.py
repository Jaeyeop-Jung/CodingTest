
def solution(prices):
    result = [i for i in range(len(prices) - 1, -1, -1)]
    stack = []
    for i, price in enumerate(prices):
        if not stack:
            stack.append([i, price])
            continue
        if stack[-1][1] <= price:
            stack.append([i, price])

        else:
            while stack and price < stack[-1][1]:
                idx, _ = stack.pop()
                result[idx] = min(result[idx], i - idx)
            stack.append([i, price])
    return result

print(solution([1, 2, 3, 2, 3]))
