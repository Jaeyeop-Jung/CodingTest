# TODO 틀림

# import random
#
#
# def sol1(arr):
#     # arr = list(map(int, input().split()))
#     if sum(arr) != 30:
#         return 0
#     arr = [[arr[i], arr[i + 1], arr[i + 2]] for i in range(0, len(arr), 3)]
#     for i in arr:
#         if sum(i) != 5:
#             return 0
#
#     # 무승부 처리
#     flag = False
#     for cur in range(len(arr)):
#         if arr[cur][1]:
#             for remove in range(len(arr)):
#                 if cur != remove and 0 < arr[remove][1]:
#                     arr[remove][1] -= 1
#                     arr[cur][1] -= 1
#                     if arr[cur][1] == 0:
#                         break
#             else:
#                 flag = True
#                 break
#         if flag:
#             break
#     if 0 < sum([i[1] for i in arr]) or flag:
#         return 0
#
#     arr.sort(key=lambda x: (-x[0], x[2]))
#     for cur in range(len(arr)):
#         if arr[cur][0]:
#             for remove in range(len(arr) - 1, -1, -1):
#                 if cur != remove and 0 < arr[remove][2]:
#                     arr[remove][2] -= 1
#                     arr[cur][0] -= 1
#                     if arr[cur][0] == 0:
#                         break
#     if 0 < sum([i[0] for i in arr]) or 0 < sum([i[2] for i in arr]):
#         return 0
#     else:
#         return 1
#
# def sol2(data):
#     from sys import stdin
#     from itertools import combinations as cb
#
#     def solution(round):
#         global ans
#         if round == 15:
#             ans = 1
#             for sub in res:
#                 if sub.count(0) != 3:
#                     ans = 0
#                     break
#             return
#
#         t1, t2 = game[round]
#         for x, y in ((0, 2), (1, 1), (2, 0)):
#             if res[t1][x] > 0 and res[t2][y] > 0:
#                 res[t1][x] -= 1
#                 res[t2][y] -= 1
#                 solution(round + 1)
#                 res[t1][x] += 1
#                 res[t2][y] += 1
#
#     game = list(cb(range(6), 2))
#     # 백트래킹
#     # data = list(map(int, stdin.readline().split()))
#     res = [data[i:i + 3] for i in range(0, 16, 3)]
#     ans = 0
#     solution(0)
#     return ans
#
# while True:
#     arr = []
#     for _ in range(6):
#         aa = 5
#         temp = []
#         while aa != 0 and len(temp) < 3:
#             num = random.randrange(0, 6)
#             if num <= aa:
#                 temp.append(num)
#                 aa -= num
#         while len(temp) < 3:
#             temp.append(0)
#         arr.append(temp)
#     arr = [arr[r][c] for r in range(6) for c in range(3)]
#     res1 = sol1(arr)
#     res2 = sol2(arr)
#     if res1 != res2:
#         print(arr)
#         print(res1, res2 )
#         break

res = []
for _ in range(4):
    arr = list(map(int, input().split()))
    if sum(arr) != 30:
        res.append(0)
        continue
    arr = [[arr[i], arr[i + 1], arr[i + 2]] for i in range(0, len(arr), 3)]
    for i in arr:
        if sum(i) != 5:
            res.append(0)
            continue

    arr.sort(key=lambda x: (-x[0], x[2]))
    dic = {i: set() for i in range(6)}
    # 무승부 처리
    flag = False
    for cur in range(len(arr)):
        if arr[cur][1]:
            for remove in range(len(arr)):
                if cur != remove and 0 < arr[remove][1]:
                    arr[remove][1] -= 1
                    arr[cur][1] -= 1
                    dic[cur].add(remove)
                    if arr[cur][1] == 0:
                        break
            else:
                flag = True
                break
        if flag:
            break
    if 0 < sum([i[1] for i in arr]) or flag:
        res.append(0)
        continue

    for cur in range(len(arr)):
        if arr[cur][0]:
            for remove in range(len(arr) - 1, -1, -1):
                if cur != remove and 0 < arr[remove][2] and remove not in dic[cur]:
                    arr[remove][2] -= 1
                    arr[cur][0] -= 1
                    if arr[cur][0] == 0:
                        break
    if 0 < sum([i[0] for i in arr]) or 0 < sum([i[2] for i in arr]):
        res.append(0)
    else:
        res.append(1)

print(*res)