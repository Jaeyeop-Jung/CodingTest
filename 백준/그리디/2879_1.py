# TODO 틀림

n = int(input())
cur = list(map(int, input().split()))
target = list(map(int, input().split()))

def getDiff(arr, target):
    return sum([abs(arr[i] - target[i]) for i in range(n)])

res = 0
for start in range(n):
    diff = abs(cur[start] - target[start])
    if diff == 0:
        continue

    best = start
    maxDiff = getDiff(cur, target)
    for end in range(start, n):
        copy = cur[:]
        for i in range(start, end + 1):
            if target[start] < cur[start]:
                copy[i] -= diff
            else:
                copy[i] += diff
        newDiff = getDiff(copy, target)
        if newDiff < maxDiff:
            best = i
            maxDiff = newDiff

    for i in range(best, start - 1, -1):
        if target[start] < cur[start]:
            cur[i] -= diff
        else:
            cur[i] += diff
    res += diff

print(res)