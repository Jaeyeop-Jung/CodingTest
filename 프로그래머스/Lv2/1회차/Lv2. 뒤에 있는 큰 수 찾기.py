
def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers) - 1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(numbers[i])

    return result



# print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
