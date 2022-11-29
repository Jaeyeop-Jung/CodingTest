

def solution(stones, k):
    start = min(stones)
    end = max(stones)
    while start <= end:
        mid = (start + end) // 2
        ablePass = True
        cnt = 0
        for i in range(len(stones)):
            if stones[i] - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                ablePass = False
                break
        if ablePass:
            start = mid + 1
        else:
            end = mid - 1

    return start


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


