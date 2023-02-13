from itertools import combinations_with_replacement

def isPalindrome(arr):
    if arr == arr[::-1]:
        return True
    return False

def solution(queries):
    result = [0] * len(queries)
    for id, query in enumerate(queries):
        maxi = sum(query)
        available = [i for i in range(1, maxi + 1) if i % 2 == 1]
        for cur in available:
            for i in combinations_with_replacement([i for i in range(len(query))], cur):
                temp = query[:]

                for each in i:
                    temp[each] -= 1
                    if temp[each] < 0:
                        break
                else:
                    if isPalindrome(temp):
                        result[id] = 1
    return result


print(solution([[1, 4, 3]]))

