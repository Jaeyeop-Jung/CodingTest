# TODO 틀림 https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python

# from bisect import bisect_right
#
# def solution(prices):
#     result = [-1] * len(prices)
#     stack = [[0, prices[0]]]
#     for i in range(1, len(prices)):
#         if stack and prices[i] < stack[-1][1]:
#             num = i - bisect_right([j[1] for j in stack], prices[i])
#             for j in range(num):
#                 if stack:
#                     index, value = stack.pop()
#                     result[index] = i - index
#         else:
#             stack.append([i, prices[i]])
#
#     for i in range(len(prices)):
#         if result[i] == -1:
#             result[i] = len(result) - i - 1
#
#     return result

def solution(prices):
    length = len(prices)

    # answer을 max값으로 초기화
    answer = [i for i in range(length - 1, -1, -1)]

    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer

print(solution([1, 2, 3, 2, 3]))
print(solution([3,4,12,4,1,5,15,4,2,4]))