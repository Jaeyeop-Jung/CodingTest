
data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(1, len(data)):
#     index = i
#     for j in range(i - 1, -1, -1):
#         if data[index] < data[j]:
#             data[index], data[j] = data[j], data[index]
#             index = j
#
# print(data)

for i in range(1, len(data)):
    for j in range(i, 0, -1):
        if data[j] < data[j-1]:
            data[j], data[j-1] = data[j-1], data[j]
        else:
            break
print(data)