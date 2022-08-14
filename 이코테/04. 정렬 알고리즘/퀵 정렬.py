import sys

sys.setrecursionlimit(10000)

data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick(pivot, start, end):
#     if end - start <= 1:
#         return
#     startFlag = False
#     endFlag = False
#     localStart = start
#     localEnd = end
#     while True:
#         if localStart >= localEnd:
#             break
#         if data[localStart] < data[pivot]:
#             localStart += 1
#         else:
#             startFlag = True
#         if data[pivot] < data[localEnd]:
#             localEnd -= 1
#         else:
#             endFlag = True
#         if startFlag and endFlag:
#             data[localStart], data[localEnd] = data[localEnd], data[localStart]
#             startFlag = False
#             endFlag = False
#     if data[localStart] <= data[localEnd]:
#         data[localStart], data[pivot] = data[pivot], data[localStart]
#     else:
#         data[localEnd], data[pivot] = data[pivot], data[localEnd]
#
#     quick(pivot, pivot + 1, localStart - 1)
#     quick(localStart, localStart + 1, end)
# quick(0, 1, len(data) - 1)

# def quick(data, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#
#         while left <= end and data[left] <= data[pivot]:
#             left += 1
#
#         while right > start and data[pivot] < data[right]:
#             right -= 1
#
#         if left >= right:
#             data[right], data[pivot] = data[pivot], data[right]
#         else:
#             data[left], data[right] = data[right], data[left]
#
#     quick(data, start, right - 1)
#     quick(data, right + 1, end)
#
# quick(data, 0, len(data) - 1)

def quick(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick(left_side) + [pivot] + quick(right_side)

print(quick(data))