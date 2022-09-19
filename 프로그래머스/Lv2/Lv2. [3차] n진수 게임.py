
def convert(n, number):
    alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    result = ''
    while number > 0:
        number, r = divmod(number, n)
        if 10 <= r < 16:
            result = alpha[r - 10] + result
        else:
            result = str(r) + result
    if result == '':
        return '0'
    return result

def solution(n, t, m, p):
    arr = []
    for i in range(t * m):
        arr.append(convert(n, i))
    arr = [arr[i][j] for i in range(len(arr)) for j in range(len(arr[i]))]
    return ''.join([arr[i] for i in range(p - 1, t * m, m)])

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
