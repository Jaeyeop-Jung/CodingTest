
# def solution(flowers):
#     day = [0] * 366
#     for start, end in flowers:
#         for i in range(start, end):
#             day[i] += 1
#
#     return len([i for i in range(len(day)) if 0 < day[i]])

def solution(flowers):
    flowers.sort(key=lambda x: (x[0], x[1]))
    result = 0
    tempStart, tempEnd = flowers[0][0], flowers[0][1]
    for i in range(1, len(flowers)):
        if flowers[i][0] <= tempEnd < flowers[i][1]:
            tempEnd = flowers[i][1]
        elif tempEnd < flowers[i][0]:
            result += tempEnd - tempStart
            tempStart, tempEnd = flowers[i][0], flowers[i][1]
    result += tempEnd - tempStart
    return result

# print(solution([[3, 4], [4, 5], [6, 7], [8, 10]]))
print(solution([[1, 2], [2, 5], [6, 7], [8, 10], [9, 11]]))