# TODO 틀림 https://bladejun.tistory.com/m/119

def solution(a):
    if len(a) == 1:
        return 0

    answer = -1
    counter = Counter(a).most_common()
    for k, v in counter:
        if (v + 1) * 2 < answer:
            break

        first = a.index(k)
        if first == 0:
            idx = first + 1



print(solution([0]))
print(solution([5,2,3,3,5,3]))
print(solution([0,3,3,0,7,2,0,2,2,0]))