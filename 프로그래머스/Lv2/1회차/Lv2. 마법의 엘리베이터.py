# TODO 틀림 잘 생각해봐 거의 맞았어

def solution(storey):
    if storey == 0:
        return 0

    arr = list(map(int, list(str(storey))))[::-1] + [0]
    result = 0
    for i in range(len(arr) - 1):
        if arr[i] <= 4:
            result += arr[i]
        elif 5 < arr[i]:
            result += (10 - arr[i])
            arr[i + 1] += 1
        elif 5 == arr[i]:
            if 5 <= arr[i + 1]:
                result += (10 - arr[i])
                arr[i + 1] += 1
            else:
                result += arr[i]
    return result + arr[-1]


# print(solution(16))
# print(solution(2554))
print(solution(555))
print(solution(554))