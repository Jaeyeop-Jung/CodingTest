# TODO 틀림 설계를 잘 해봐 할 수 있어

from itertools import combinations

def solution(relation):
    relation = [tuple(relation[r][c] for r in range(len(relation))) for c in range(len(relation[0]))]

    result = set()
    for num in range(1, len(relation[0]) + 1):
        for columns in combinations([i for i in range(0, len(relation))], num):
            # 유일성 테스트
            temp = [tuple(relation[column][i] for column in columns) for i in range(len(relation[0]))]
            if len(temp) != len(set(temp)):
                continue
            # 최소성 테스트
            for i in result:
                if set(i) & set(columns) == set(i):
                    break
            else:
                result.add(columns)

    return len(result)


# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution([
    ["a","1","aaa","c","ng"],
    ["a","1","bbb","e","g"],
    ["c","1","aaa","d","ng"],
    ["d","2","bbb","d","ng"]]))