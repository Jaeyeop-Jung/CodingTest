# TODO 틀림

def solution(n, l, r):
    if n == 1:
        return '11011'[l - 1:r].count('1')
    s = '11011' * 2 + '00000' + '11011' * 2



print(solution(2, 4, 17))
