# TODO 틀림

def solution(begin, end):
    result = []
    for i in range(begin, end + 1):
        if i == 1:
            result.append(0)
            continue
        # 소수가 아니라면
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                if i // j <= 10000000:
                    result.append(i // j)
                    break
        else:
            result.append(1)
    return result

# def solution(begin, end):
#     result = []
#     for i in range(begin, end + 1):
#         if i == 1:
#             result.append(0)
#             continue
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 if i // j <= 10000000:
#                     result.append(i // j)
#                     break
#         else:
#             result.append(1)
#     return result

print(solution(1, 10))