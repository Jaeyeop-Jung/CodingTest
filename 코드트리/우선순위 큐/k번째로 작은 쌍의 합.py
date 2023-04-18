# TODO 틀림

# import heapq
#
# n, m, k = map(int, input().split())
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
#
# heapq.heapify(arr1)
# heapq.heapify(arr2)
#
# temp = []
# for _ in range(k):
#     last = heapq.heappop(arr1)
#     heapq.heappush(temp, last)
#     if not arr1:
#         arr1 = temp
#         heapq.heappop(arr2)
#
# print(last + heapq.heappop(arr2))

import heapq

# 입력:
n, m, k = tuple(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# 변수 선언
pq = []

# 주어진 배열을 정렬해줍니다.
arr1 = sorted(arr1)
arr2 = sorted(arr2)

# 처음에는 n개의 원소에 대해 각각
# 두 번째 수열의 첫 번째 원소를 대응시켜줍니다.
# 작은 값이 더 먼저 나와야 하므로
# +를 붙여서 넣어줍니다.
for i in range(n):
    heapq.heappush(pq, (arr1[i] + arr2[0], i, 0))

# 1번부터 k - 1번까지 합이 작은 쌍을 골라줍니다.
for i in range(k - 1):
    _, idx1, idx2 = heapq.heappop(pq)

    # 만약 첫 번째 수열의 idx1번째 원소와 더 매칭할 두 번째 수열의 원소가 남아있다면
    # 우선순위 큐에 넣어줍니다.
    idx2 += 1
    if idx2 < m:
        heapq.heappush(pq, (arr1[idx1] + arr2[idx2], idx1, idx2))

# k번째 합을 가져옵니다.
pair_sum, _, _ = heapq.heappop(pq)

print(pair_sum)