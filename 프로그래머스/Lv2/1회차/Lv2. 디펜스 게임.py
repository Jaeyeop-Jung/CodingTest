# TODO 틀림 아이디어는 맞았는데 구현을 더 잘해봐

def solution(n, k, enemy):
    idx = 0
    h = []
    while idx < len(enemy):
        n -= enemy[idx]
        heapq.heappush(h, -enemy[idx])
        if n < 0:
            if 0 < k:
                n -= heapq.heappop(h)
                idx += 1
                k -= 1
                continue
            else:
                break
        idx += 1
    return idx

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(3, 1, [3,2,2]))
print(solution(2, 4, [3,3,3,3]))
print(solution(8, 3, [1,2,2,2,10,11]))
print(solution(1, 4, [10,2,2,2,10,11]))