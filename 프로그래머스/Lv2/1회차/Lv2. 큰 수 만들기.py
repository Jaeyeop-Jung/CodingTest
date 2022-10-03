# TODO 틀림

# from itertools import permutations
#
# def solution(number, k):
#     number = [[i, number[i]] for i in range(len(number))]
#     result = 0
#     for i in permutations(number, len(number) - k):
#         temp = ''
#         for j in range(len(list(i))):
#             if j == len(list(i)) - 1:
#                 temp += i[j][1]
#                 continue
#             if i[j][0] > i[j + 1][0]:
#                 break
#             temp += i[j][1]
#         else:
#             result = max(result, int(temp))
#     return result

# def solution(number, k):
#     first = [int(number[i]) for i in range(k)]
#     idx = 0
#     tempMax = 0
#     for i in range(len(first)):
#         if tempMax < first[i]:
#             idx = i
#             tempMax = first[i]
#     number = number[idx:]
#     k -= idx
#     for i in range(len(number) - 1):
#         if k == 0:
#             break
#         good = False
#         for j in range(i + 1, len(number)):
#             if number[i] < number[j]:
#                 good = True
#                 break
#         if good:
#             number = number[:i] + number[i + 1:]
#             k -= 1
#     for i in range(k):
#         numberList = [int(number[i]) for i in range(len(number))]
#         numberList.pop(numberList.index(min(numberList)))
#         number = ''.join([str(i) for i in numberList])
#     return number

# def solution(number, k):
#     resultLength = len(number) - k
#     result = []
#     left = 0
#     while not len(result) == len(number) - k:
#         idx = 0
#         tempMax = 0
#         for i in range(left, len(number) - resultLength + 1):
#             if tempMax < int(number[i]):
#                 idx, tempMax = i, int(number[i])
#         result.append(number[idx])
#         resultLength -= 1
#         left = idx + 1
#     return ''.join(result)

def solution(number, k):
    answer = []  # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    print(''.join(answer[:len(answer) - k]))


print(solution('12', 1))
print(solution('987654321', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))
print(solution('942051', 2))