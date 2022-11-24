# TODO 틀림 생각을 더 잘 해봐

def solution(n, cores):
    if n <= len(cores):
        return n

    n -= len(cores)
    start = 1
    end = 50000
    while start <= end:
        mid = (start + end) // 2
        eachN = sum([mid // i for i in cores])
        if eachN < n:
            start = mid + 1
        else:
            end = mid - 1


    worked = sum([(start - 1) // i for i in cores])
    while True:
        for i in range(len(cores)):
            if start % cores[i] == 0:
                worked += 1
                if worked == n:
                    return i + 1
        start += 1


print(solution(6, [1, 2, 3]))
# print(solution(10, [3, 2, 4]))
# print(solution(10, [1, 1]))
