# TODO 틀림 https://rrojin.tistory.com/46

n = int(input())
preArr = list(map(int, input().split()))

target = preArr[:]
for i in range(n - 1, 0, -1):
    if target[i-1] < target[i]:
        for j in range(n - 1, 0, -1):
            if target[i-1] < target[j]:
                target[j], target[i-1] = target[i-1], target[j]
                target = target[:i] + sorted(target[i:])
                print(*target)
                exit()

print(-1)


