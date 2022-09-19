from itertools import permutations

def solution(k, dungeons):
    result = 0
    for i in permutations(dungeons):
        temp = 0
        tempK = k
        for j in list(i):
            if 0 <= tempK - j[0]:
                temp += 1
                tempK -= j[1]
        result = max(result, temp)
    return result

print(solution(80, [[80,20],[50,40],[30,10]]))