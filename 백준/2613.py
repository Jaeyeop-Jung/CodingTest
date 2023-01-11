# TODO 틀림 맞출 수 있었는데 더 고민

n, m, = map(int, input().split())
arr = list(map(int, input().split()))

# if m == 1:
#     print(sum(arr))
#     print(n)
#     exit()
# elif n == m:
#     print(max(arr))
#     print(*[1] * m)
#     exit()

def getGroup():
    total, eachCnt, groupCnt = 0, 0, 0
    dp = []
    idx = 0
    while idx < len(arr):
        if total + arr[idx] <= mid:
            total += arr[idx]
            eachCnt += 1
            idx += 1
        else:
            dp.append(eachCnt)
            total = 0
            eachCnt = 0
            groupCnt += 1
    if eachCnt != 0:
        groupCnt += 1
        dp.append(eachCnt)

    return groupCnt

# 이진 탐색으로 최대값을 구함(이름 = start)
start = max(arr)
end = sum(arr)
while start <= end:
    mid = (start + end) // 2
    cnt = getGroup()
    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1


groupCnt = [1] * n
removed = [False] * n
for i in range(len(arr)):
    # 제거되지 않고 합쳐진 그룹의 개수가 m과 같으면 출력 후 종료
    if removed.count(False) == m:
        print(start)
        for k in range(len(groupCnt)):
            if not removed[k]:
                print(groupCnt[k], end=' ')
        exit()

    # 삭제 되었으면 넘김
    if removed[i]:
        continue

    for j in range(i + 1, len(arr)):
        # 삭제 되었으면 넘김
        if removed[j]:
            break

        # 그룹을 합쳐도 되면 합침
        if arr[i] + arr[j] <= start:
            removed[j] = True
            groupCnt[i] += 1
            arr[i] += arr[j]

        # 그룹을 합쳐서 넘으면 종료
        else:
            break