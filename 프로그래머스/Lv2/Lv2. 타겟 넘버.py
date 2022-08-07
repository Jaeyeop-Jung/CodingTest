result = 0

def solution(numbers, target):
    def dfs(curProcess, sum):
        global result
        if curProcess == n:
            if sum == target:
                result += 1
            return
        else:
            dfs(curProcess + 1, sum + numbers[curProcess])
            dfs(curProcess + 1, sum - numbers[curProcess])

    n = len(numbers)
    dfs(0, 0)
    return result

print(solution([4, 1, 2, 1], 4))