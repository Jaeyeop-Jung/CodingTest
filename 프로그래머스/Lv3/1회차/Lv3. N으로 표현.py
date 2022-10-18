# TODO 틀림

def solution(N, number):
    if number == 1:
        return 1

    dp = []
    for n in range(1, 9):
        temp = set()
        temp.add(int(str(N) * n))
        for i in range(n - 1):
            for op1 in dp[i]:
                for op2 in dp[-i - 1]:
                    temp.add(op1 + op2)
                    temp.add(op1 - op2)
                    temp.add(op1 * op2)
                    if op2 != 0:
                        temp.add(op1 // op2)
        if number in temp:
            return n
        dp.append(temp)
    return -1


print(solution(5, 12))
print(solution(2, 11))