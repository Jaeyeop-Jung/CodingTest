# TODO 틀림 

# def solution(queue1, queue2):
#     arr = queue1 + queue2
#     start, end = len(queue1) ** 2, len(queue1) ** 2
#     answer = 0
#     for i in range(len(arr) - 1):
#         for j in range(i, len(arr)):
#             if sum(arr[i:j]) == sum(arr) / 2:
#                 if i < start and j - len(queue1) < end:
#                     answer = i + j - len(queue1)
#                     start = i
#                     end = j
#     if answer == 0:
#         return -1
#     else:
#         return answer


from collections import deque
def solution(queue1, queue2):
    target = sum(queue1 + queue2) / 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    for i in range(len(queue1) ** 2):
        if sum1 == sum2:
            return i
        elif sum1 < target:
            pop = q2.popleft()
            q1.append(pop)
            sum1 += pop
            sum2 -= pop
        else:
            pop = q1.popleft()
            q2.append(pop)
            sum1 -= pop
            sum2 += pop
    return -1

solution([3, 2, 7, 2], [4, 6, 5, 1])