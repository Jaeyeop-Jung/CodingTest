

def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)

    result = 0
    aIdx = 0
    bIdx = 0
    while bIdx < len(B) and aIdx < len(A):
        if A[aIdx] < B[bIdx]:
            result += 1
            bIdx += 1
        aIdx += 1

    return result


print(solution([5,1,3,7], [2,2,6,8]))

