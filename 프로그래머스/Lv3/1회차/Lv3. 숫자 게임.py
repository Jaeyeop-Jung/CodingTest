from collections import deque

def solution(A, B):
    result = 0

    A.sort(reverse=True)
    B.sort(reverse=True)

    A = deque(A)
    B = deque(B)

    aIdx = 0
    bIdx = 0
    while True:
        if len(A) == 0 and len(B) == 0:
            break

        if B[bIdx] <= A[aIdx]:
            B.pop()
            A.popleft()
        else:
            A.popleft()
            B.popleft()
            result += 1
    return result

print(solution([5,1,3,7], [2,2,6,8]))
print(solution([2,2,2,2], [1,1,1,1]))