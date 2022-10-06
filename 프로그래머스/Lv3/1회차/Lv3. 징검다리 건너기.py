# TODO 틀림

def solution(stones, k):
    result = max(stones) + 1
    start = 0
    end = max(stones) + 1
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in stones:
            if i - mid <= 0:
                cnt += 1
            else:
                cnt = 0
            if k <= cnt:
                break
        else:
            start = mid + 1
            continue
        result = min(result, mid)
        end = mid - 1
    return result

# from collections import deque
#
# def solution(stones, k):
#     result = max(stones) + 1
#     q = deque(stones[0:k - 1])
#     for i in range(k - 1, len(stones)):
#         q.append(stones[i])
#         result = min(result, max(q))
#         q.popleft()
#     return result


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

