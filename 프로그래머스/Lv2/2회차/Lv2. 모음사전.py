from itertools import product

def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    arr.sort()

    dic = []
    for i in range(1, 6):
        for j in product(arr, repeat=i):
            dic.append(''.join(j))
    dic.sort()
    return dic.index(word) + 1



print(solution("AAAAE"))