# TODO 틀림

from itertools import combinations

def solution(relation):
    result = 0
    arr = [[] for i in range(len(relation[0]))]
    for i in relation:
        for j in range(len(i)):
            arr[j].append(i[j])
    good = []
    for i in range(1, len(relation[0]) + 1):
        for j in combinations([i for i in range(1, len(relation[0]) + 1)], i):
            total = [''] * len(relation)
            tempGood = ''
            for k in list(j):
                same = len(list(j))
                if len(j) != 1:
                    tempGood = ''.join([str(z) for z in j])
                    for i in good:
                        same = len(i)
                        for j in i:
                            if j in tempGood:
                                same -= 1
                        if same == 0:
                            break

                else:
                    tempGood = str(k)
                if same == 0:
                    break
                temp = [''] * len(relation)
                for x in range(len(relation)):
                    temp[x] += arr[k - 1][x] + '/'
                if len(j) != 1 and len(temp) == len(set(temp)):
                    break
                elif len(j) == 1 and len(temp) != len(set(temp)):
                    break
                total = [''.join(list(i)) for i in zip(total, temp)]
            else:
                if len(total) == len(set(total)):
                    result += 1
                    good.append(tempGood)

    return result

# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
print(solution(
    [
        ["a","1","aaa","c","ng"],
        ["a","1","bbb","e","g"],
        ["c","1","aaa","d","ng"],
        ["d","2","bbb","d","ng"]
    ])
)