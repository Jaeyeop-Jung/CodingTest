
arr = list(input())
n = len(arr)

# idx = 0
# while idx < n:
#     if arr[idx] == '0':
#         if idx + 1 < n and arr[idx + 1] == '1':
#             idx += 2
#         else:
#             print('NOISE')
#             exit()
#
#     else:
#         if idx + 1 < n and arr[idx + 1] == '0':
#             idx += 2
#             cnt = 0
#             while idx < n and arr[idx] == '0':
#                 cnt += 1
#                 idx += 1
#             if cnt == 0:
#                 print('NOISE')
#                 exit()
#             cnt = 0
#             while idx < n and arr[idx] == '1':
#                 cnt += 1
#                 idx += 1
#             if cnt == 0:
#                 print('NOISE')
#                 exit()
#         else:
#             print('NOISE')
#             exit()
# print('SUBMARINE')

def dfs(arr, idx):
    if idx == n:
        print('SUBMARINE')
        exit()

    if arr[idx] == '0':
        if idx + 1 < n and arr[idx + 1] == '1':
            dfs(arr, idx + 2)
    else:
        if idx + 1 < n and arr[idx + 1] == '0':
            next = idx + 2
            while next < n and arr[next] == '0':
                next += 1
            if next != idx + 2:
                while next < n and arr[next] == '1':
                    next += 1
                    dfs(arr, next)

dfs(arr, 0)
print('NOISE')