
def solution(data, col, row_begin, row_end):
    data_sort = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    temp = []
    for i in range(row_begin - 1, row_end):
        temp.append(sum([j % (i + 1) for j in data_sort[i]]))

    result = temp[0]
    for i in range(1, len(temp)):
        result ^= temp[i]
    return result


print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))
