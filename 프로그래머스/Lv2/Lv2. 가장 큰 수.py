# 틀림

def solution(numbers):
    temp = [[str(numbers[i]), i] for i in range(len(numbers))]
    maxIndex = max([len(temp[i][0]) for i in range(len(temp))])
    for i in range(len(temp)):
        for j in range(maxIndex - len(temp[i][0])):
            temp[i][0] += temp[i][0][0]

    temp.sort(reverse=True, key=lambda x: int(x[0]))

    result = ''
    for _, j in temp:
        result += str(numbers[j])
    return str(int(result))


print(solution([23, 232, 21, 212] ))

# 23232 21221
# 23232 21212