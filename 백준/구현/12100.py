
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def rotate(arr, d):
    if d == 0:
        return [i[:] for i in arr]
    if 0 < d:
        newArr = []
        for c in range(n):
            temp = []
            for r in range(n - 1, -1, -1):
                temp.append(arr[r][c])
            newArr.append(temp)
    else:
        newArr = []
        for c in range(n - 1, -1, -1):
            temp = []
            for r in range(n):
                temp.append(arr[r][c])
            newArr.append(temp)
    return newArr

def push(arr):
    tempArr = [i[:] for i in arr]
    for r in range(n):
        temp = []
        for c in range(n):
            if tempArr[r][c] != 0:
                temp.append(tempArr[r][c])
        newTemp = []
        while 2 <= len(temp):
            if temp[-1] == temp[-2]:
                newTemp.insert(0, temp.pop() + temp.pop())
            else:
                newTemp.insert(0, temp.pop())
        while temp:
            newTemp.insert(0, temp.pop())
        while len(newTemp) < n:
            newTemp.insert(0, 0)
        tempArr[r] = newTemp
    return tempArr

result = 0
def dfs(arr, cnt, route):
    if cnt <= 5:
        global result
        result = max(result, max(map(max, arr)))
    else:
        return
    for i in range(4):
        tempArr = rotate(arr, 0)
        for _ in range(i):
            tempArr = rotate(tempArr, -i)
        tempArr = push(tempArr)
        for _ in range(i):
            tempArr = rotate(tempArr, i)
        dfs(tempArr, cnt + 1, route + [i])

dfs(arr, 0, [])
print(result)