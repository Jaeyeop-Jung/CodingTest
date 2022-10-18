
def solution(want, number, discount):
    result = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    dp = {}
    for i in range(len(discount)):
        dp[discount[i]] = dp.get(discount[i], 0) + 1
        if 10 <= i:
            dp[discount[i - 10]] -= 1

        for key in dic:
            if key not in dp or dp[key] < dic[key]:
                break
        else:
            result += 1

    return result





print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))