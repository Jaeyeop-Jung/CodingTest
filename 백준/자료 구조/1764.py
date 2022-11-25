

n, m = map(int, input().split())
dic = {}
for i in range(n):
    dic[input()] = True

resultArr = []
for i in range(m):
    s = input()
    if s in dic:
        resultArr.append(s)

resultArr.sort()
print(len(resultArr))
for i in range(len(resultArr)):
    print(resultArr[i])

