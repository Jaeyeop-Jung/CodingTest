# TODO 틀림 더 생각해봐 할 수 있어

from itertools import combinations

def solution(relation):
    tempResult = []
    for num in range(1, len(relation[0]) + 1):
        for comb in combinations([i for i in range(len(relation[0]))], num):
            temp = [[] for i in range(len(relation))]
            for i in range(len(relation)):
                for j in list(comb):
                    temp[i].append(relation[i][j])
            duplicate = []
            for i in temp:
                if i not in duplicate:
                    duplicate.append(i)

            if len(temp) != len(duplicate): # 중복 테스트
                continue
            tempResult.append(comb)

    result = set()
    for i in tempResult:
        if not result:
            result.add(tuple(i))
            continue
        for j in result:
            if set(j) & set(i) == set(j):
                break
        else:
            result.add(tuple(i))

    return len(result)




# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
# print(solution([['100', 'a'], ['100', 'b']]))
print(solution([
    ["a","1","aaa","c","ng"],
    ["a","1","bbb","e","g"],
    ["c","1","aaa","d","ng"],
    ["d","2","bbb","d","ng"]]))