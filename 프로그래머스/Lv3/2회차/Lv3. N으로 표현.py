# TODO 틀림

cal = ['+', '-', '*', '//']

def solution(n, number):
    if n == number:
        return 1

    result = [set() for i in range(9)]
    result[1].add(n)

    for i in range(2, 9):
        for j in range(1, i):
            for c1 in result[j]:
                for c2 in result[i - j]:
                    for k in cal:
                        if k == '//' and c2 == 0:
                            continue
                        temp = eval(str(c1) + k + str(c2))
                        if temp == number:
                            return i
                        result[i].add(temp)
        nM = int(str(n) * i)
        if nM == number:
            return i
        result[i].add(nM)
    return -1

print(solution(5, 12))
print(solution(2, 11))