#
# n = int(input())
# cnt = 0
# cycle = 0
# arr = []
# while cnt < n:
#     for i in range(6):
#         arr.append(int(str(cycle) + str(i) + '666'))
#         cnt += 1
#     for i in range(10):
#         arr.append(int(str(cycle) + '666' + str(i)))
#         cnt += 1
#     for i in range(7, 10):
#         arr.append(int(str(cycle) + str(i) + '666'))
#         cnt += 1
#     cycle += 1
#
# print(arr[n - 1])

n = int(input())
cnt = 0
last = 0
while cnt < n:
    while True:
        last += 1
        if '666' in str(last):
            break
    cnt += 1
print(last)