from collections import defaultdict

def solution(N, number):
    dp = defaultdict(set)
    dp[1].add(N)

    total = set()
    for cur in range(2, 9):
        for i in range(1, cur):
            j = cur - i
            for num1 in dp[i]:
                for num2 in dp[j]:
                    next = num1 + num2
                    if next not in total:
                        dp[cur].add(next)
                        total.add(next)

                    next = num1 - num2
                    if next not in total:
                        dp[cur].add(next)
                        total.add(next)

                    next = num1 * num2
                    if next not in total:
                        dp[cur].add(next)
                        total.add(next)

                    if num2 != 0:
                        next = num1 // num2
                        if next not in total:
                            dp[cur].add(next)
                            total.add(next)

        for i in range(1, cur):
            j = cur - i
            num1 = str(N) * i
            num2 = str(N) * j

            next = eval(num1 + '+' + num2)
            if next not in total:
                dp[cur].add(next)
                total.add(next)

            next = eval(num1 + '-' + num2)
            if next not in total:
                dp[cur].add(next)
                total.add(next)

            next = eval(num1 + '*' + num2)
            if next not in total:
                dp[cur].add(next)
                total.add(next)

            next = eval(num1 + '//' + num2)
            if next not in total:
                dp[cur].add(next)
                total.add(next)

        if str(N) * cur not in total:
            dp[cur].add(int(str(N) * cur))
            total.add(int(str(N) * cur))

    for i in range(1, 9):
        if number in dp[i]:
            return i
    return -1

print(solution(5, 5555))