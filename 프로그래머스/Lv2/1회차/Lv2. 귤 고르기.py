from collections import defaultdict

def solution(k, tangerine):
    tangerine.sort()
    dic = defaultdict(int)
    for i in tangerine:
        dic[i] += 1
    arr = [[dic[i], i] for i in dic]
    arr.sort(key=lambda x: -x[0])

    temp = 0
    result = 0
    for v, i in arr:
        result += 1
        temp += v
        if k <= temp:
            return result


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
