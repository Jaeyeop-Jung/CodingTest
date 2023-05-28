# TODO 틀림 이건 좀 깊게 잘 생각해봐라

n = int(input())
arr = [[i, input()] for i in range(n)]

sortArr = sorted(arr, key=lambda x: x[1])

# 최대 접두사 길이가 0인 경우를 위해 index = 0, 1을 초기값으로 줌
flag = False
for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i][1] == arr[j][1]:
            continue
        flag = True
        resultCnt = 0
        for k in range(min(len(arr[i][1]), len(arr[j][1]))):
            if arr[i][1][k] != arr[j][1][k]:
                break
            resultCnt += 1
        result = [i, j]
        break
    if flag:
        break

for i in range(n - 1):
    # 같은 단어이면 스킵
    left = sortArr[i]
    right = sortArr[i + 1]
    if left[1] == right[1]:
        continue

    # 접두사 길이 체크
    tempCnt = 0
    for j in range(min(len(left[1]), len(right[1]))):
        if left[1][j] != right[1][j]:
            break
        tempCnt += 1

    # 기존보다 접두사가 더 길면
    temp = sorted([left[0], right[0]])
    if resultCnt < tempCnt:
        resultCnt = tempCnt
        result = temp
    # 현재 결과의 index보다 더 작은 index의 단어이면 갱신
    elif resultCnt == tempCnt and temp < result:
        result = temp


print(arr[result[0]][1])
print(arr[result[1]][1])