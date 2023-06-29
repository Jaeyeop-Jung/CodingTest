# TODO 틀림 잘 생각해봐 다음엔 맞자

from collections import defaultdict

def solution(N, number):
    dic = defaultdict(set)
    dic[1].add(int(N))

    if N == number:
        return 1

    for cur in range(2, 9):
        dic[cur].add(int(str(N) * cur))
        for l in range(1, cur + 1):
            r = cur - l

            for left in dic[l]:
                for right in dic[r]:
                    dic[cur].add(left + right)
                    dic[cur].add(left - right)
                    dic[cur].add(left * right)
                    if right != 0:
                        dic[cur].add(left // right)
        if number in dic[cur]:
            return cur

    return -1


# print(solution(5, 12))
# print(solution(2, 11))
# print(solution(8, 5800))
print(solution(8, 8))
