# TODO 틀림

def solution(n, cores):
    if n <= len(cores):
        return n
    n -= len(cores)
    start = 0
    end = n * max(cores)
    while start <= end:
        mid = (start + end) // 2
        finished = sum([mid // i for i in cores])
        if finished < n - 1:
            start = mid + 1
        else:
            end = mid - 1

    cnt = 0
    for i in cores:
        cnt += (start - 1) // i

    while True:
        for i, value in enumerate(cores):
            if start % value == 0:
                cnt += 1
                if cnt == n:
                    return i + 1
        start += 1

# print(solution(6, [1,2,3]))
print(solution(10, [1,2,10]))
# print(solution(5, [4540, 6383, 8674, 2699]))