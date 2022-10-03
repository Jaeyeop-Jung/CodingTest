# result = 0
#
# def solution(numbers, target):
#     def dfs(curProcess, sum):
#         global result
#         if curProcess == n:
#             if sum == target:
#                 result += 1
#             return
#         else:
#             dfs(curProcess + 1, sum + numbers[curProcess])
#             dfs(curProcess + 1, sum - numbers[curProcess])
#
#     n = len(numbers)
#     dfs(0, 0)
#     return result

def solution(numbers, target):
    global result
    result = 0

    def dfs(idx, sum):
        global result
        if idx == len(numbers) - 1:
            if sum + numbers[idx] == target:
                result += 1
            if sum - numbers[idx] == target:
                result += 1
            return
        dfs(idx + 1, sum + numbers[idx])
        dfs(idx + 1, sum - numbers[idx])

    dfs(0, 0)
    return result

print(solution([4, 1, 2, 1], 4))