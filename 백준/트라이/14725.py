
n = int(input())
arr = [list(input().split()) for _ in range(n)]

dic = {}
for i in range(len(arr)):
    cur = dic
    for depth in range(1, int(arr[i][0]) + 1):
        if arr[i][depth] not in cur:
            cur[arr[i][depth]] = {}
        cur = cur[arr[i][depth]]


def getPrint(dic, depth):
    if not dic:
        return
    keys = sorted(dic.keys())
    for key in keys:
        print('--' * depth + key)
        getPrint(dic[key], depth + 1)


getPrint(dic, 0)

