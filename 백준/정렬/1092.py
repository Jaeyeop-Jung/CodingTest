import sys

input = sys.stdin.readline

n = int(input())
crains = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

crains.sort()
if crains[-1] < max(boxes): # 불가능한 경우 끝냄
    print(-1)
    exit()

cnt = [0] * 1_000_001 # 옮겨야 될 박스 갯수 카운트
for i in boxes:
    cnt[i] += 1

arr = []
cur = 0
for i in crains:    # 크레인 별로 몇개의 박스를 옮겨야 되는지 저장
    arr.append(sum(cnt[cur:i + 1]))
    cur = i + 1

res = 0
while True:
    # 모두 옮겼으면 끝냄
    for i in arr:
        if i != 0:
            break
    else:
        break

    # 옮겨야 될게 있으면
    res += 1
    cnt = 1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0: # 해당 크레인이 자신의 무게를 이미 들었으면 더 작은 크레인의 박스를 대신 들어주기위해 cnt + 1
            cnt += 1
        else:
            if cnt <= arr[i]:
                arr[i] -= cnt
                cnt = 1
            else:   # 남은 크레인 다음으로 넘기기
                cnt -= arr[i]
                cnt += 1
                arr[i] = 0

print(res)