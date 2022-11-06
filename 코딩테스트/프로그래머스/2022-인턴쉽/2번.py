
def indexOf(studentNum, arr):
    for i in range(len(arr)):
        if arr[i][0] == studentNum:
            return i

def solution(n, student, point):
    result = 0
    arr = [[i, 0] for i in range(1, n + 1)]

    for i in range(len(student)):
        index = indexOf(student[i], arr)
        arr[index][1] += point[i]

        arr.sort(key=lambda x: (-x[1], x[0]))
        nextIndex = indexOf(student[i], arr)

        if index <= n // 2 - 1 and n // 2 - 1 < nextIndex:
            result += 1
        elif n // 2 - 1 < index and nextIndex <= n // 2 - 1:
            result += 1
    return result

# print(solution(6, [6,1,4,2,5,1,3,3,1,6,5], [3,2,5,3,4,2,4,2,3,2,2]))
print(solution(10, [3, 2, 10, 2, 8, 3, 9, 6, 1, 2], [3, 2, 2, 5, 4, 1, 2, 1, 3, 3]))