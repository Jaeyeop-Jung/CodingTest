
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def bomb(arr):
    flag = False
    for c in range(n):
        for start in range(n):
            if arr[start][c] == 0:
                continue
            for end in range(start, n):
                if arr[start][c] != arr[end][c]:
                    if m <= end - start:
                        for i in range(start, end):
                            arr[i][c] = 0
                            flag = True
                    break
            else:
                if m <= end - start + 1:
                    for i in range(start, end + 1):
                        arr[i][c] = 0
                    flag = True
    return flag

def down():
    for c in range(n):
        temp = []
        for r in range(n):
            if arr[r][c] != 0:
                temp.append(arr[r][c])
        down = n - 1 - len(temp)
        for r in range(n - 1, down, -1):
            arr[r][c] = temp.pop()
        for r in range(down, -1, -1):
            arr[r][c] = 0

def rotate():
    global arr
    newArr = []
    for c in range(n):
        temp = []
        for r in range(n - 1, -1, -1):
            temp.append(arr[r][c])
        newArr.append(temp)
    arr = newArr

for _ in range(k):
    while bomb(arr):
        down()
    rotate()
    down()
while bomb(arr):
    down()

result = 0
for i in arr:
    result += i.count(0)
print(n * n - result)
