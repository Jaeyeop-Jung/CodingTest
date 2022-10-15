# TODO 틀림

def canFix(n, fixed, start, move):
    result = 0
    cnt = 0
    while cnt < move + 1:
        if fixed[(start + cnt) % n] is False:
            result += 1
        cnt += 1
    return result

def findNextWeak(n, fixed, start):
    cnt = 0
    while cnt < n:
        if fixed[(start + cnt) % n] is False:
            return (start + cnt) % n
        cnt += 1
    return -1

def solution(n, weak, dist):
    result = 0

    weak.sort()
    maxTerm, start, end = 0, 0, 0
    for i in range(len(weak) - 1):
        if maxTerm < weak[i + 1] - weak[i]:
            maxTerm = weak[i + 1] - weak[i]
            start = weak[i + 1]
            end = weak[i]

    fixed = [True] * n
    for i in weak:
        fixed[i] = False

    dist.sort(reverse=True)
    while False in fixed:
        if not dist:
            break

        maxFixCnt = canFix(n, fixed, start, dist[0])
        idx = 0
        for i in range(1, len(dist)):
            tempFixCnt = canFix(n, fixed, start, dist[i])
            if maxFixCnt == tempFixCnt:
                idx = i
            else:
                break

        pop = dist.pop(idx)
        result += 1
        for i in range(start, start + pop + 1):
            fixed[i % n] = True

        start = findNextWeak(n, fixed, start)
    else:
        return result
    return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# print(solution(12, [10,0], [1,2]))
# print(solution(30, [0, 3, 11, 21], [10, 4]))