
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        temp = 0
        for j in range(i, n + 1):
            temp += j
            if n < temp:
                break
            elif temp == n:
                answer += 1
                break
    return answer

print(solution(15))