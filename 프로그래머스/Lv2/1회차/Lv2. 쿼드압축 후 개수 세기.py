
def solution(arr):
    if len(arr) == 1:
        return arr[0][0]

    result = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] = [arr[i][j], False]

    bound = len(arr)
    while bound != 0:
        if bound == 1:
            for i in range(len(arr)):
                for j in range(len(arr)):
                    if arr[i][j][1] is False:
                        result.append(arr[i][j][0])
                        arr[i][j][1] = True
            break


        for i in range(0, len(arr), bound):
            for j in range(0, len(arr), bound):
                if arr[i][j][1] is True:
                    continue
                value = arr[i][j][0]
                same = True
                for row in range(i, i + bound):
                    for column in range(j, j + bound):
                        if arr[row][column][0] != value:
                            same = False
                            break
                    if same is False:
                        break
                else:
                    result.append(value)
                    for row in range(i, i + bound):
                        for column in range(j, j + bound):
                            arr[row][column][1] = True
        bound //= 2

    return [result.count(0), result.count(1)]


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
# print(solution([[0, 0], [0, 0]]))

