# TODO 틀림 잘 생각해봐라 맞출 수 있다

n = int(input())
arr = list(map(int, input().split()))

# if sum(arr) % 3 != 0:
#     print('NO')
#     exit()
#
# for i in range(n):
#     if 1 <= arr[i] // 3:
#         arr[i] = arr[i] % 3 + 3
#
# while True:
#     for i in range(n):
#         if 0 < arr[i] and arr[i] % 2 == 0:
#             arr[i] -= 2
#             break
#     else:
#         for i in range(n):
#             if 2 <= arr[i]:
#                 arr[i] -= 2
#                 break
#         else:
#             break
#
#     for i in range(n):
#         if 0 < arr[i] and arr[i] % 2 != 0:
#             arr[i] -= 1
#             break
#     else:
#         for i in range(n):
#             if 0 < arr[i]:
#                 arr[i] -= 1
#                 break



print('YES' if sum(arr) == 0 else 'NO')