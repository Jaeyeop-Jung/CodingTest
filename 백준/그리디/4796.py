
arr = []
while True:
    l, p, v, = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    arr.append([l, p, v])

case = 1
while case <= len(arr):
    l, p, v = arr[case - 1]
    result = v // p * l
    result += min(v % p, l)
    print('Case' + ' ' + str(case) + ': ' + str(result))
    case += 1
