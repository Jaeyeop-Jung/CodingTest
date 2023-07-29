# TODO 틀림 잘 생각해봐 문제를 더 정확히 파악하면 할 수 있다

n = int(input())

curN = 0
totalLength = 3
while totalLength < n:
    curN += 1
    totalLength = totalLength * 2 + curN + 3

def recur(total, mid, n):
    if n <= 3:
        return 'moo'[n - 1]

    left = (total - mid) // 2
    if n <= left:
        return recur(left, mid - 1, n)
    if left + mid < n:
        return recur(left, mid - 1, n - left - mid)

    if n - left == 1:
        return 'm'
    else:
        return 'o'

print(recur(totalLength, curN + 3, n))
