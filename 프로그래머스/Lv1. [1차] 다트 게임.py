
def solution():
    result = []
    index = -1
    inputList = list(input())
    flag = False
    for i in range(len(inputList)):
        if str(inputList[i]).isnumeric():
            if flag:
                result[index] = int(str(result[index]) + str(inputList[i]))
                flag = False
                continue
            result.append(int(inputList[i]))
            index += 1
            flag = True
            continue
        if str(inputList[i]) == 'S':
            flag = False
            continue
        if str(inputList[i]) == 'D':
            result[index] = result[index] ** 2
            flag = False
            continue
        elif str(inputList[i]) == 'T':
            result[index] = result[index] ** 3
            flag = False
            continue
        if str(inputList[i]) == '*':
            if index == 0:
                result[index] *= 4
                flag = False
            else:
                result[index - 1] *= 2
                result[index] *= 2
                flag = False
        elif str(inputList[i]) == '#':
            result[index] = -result[index]
            flag = False

    print(sum(result))

solution()