from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    for i in range(len(queue1) * 3):
        if sum2 == sum1:
            return i
        elif sum1 < sum2:
            pop = queue2.popleft()
            queue1.append(pop)
            sum1 += pop
            sum2 -= pop
        else:
            pop = queue1.popleft()
            queue2.append(pop)
            sum1 -= pop
            sum2 += pop
    return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))