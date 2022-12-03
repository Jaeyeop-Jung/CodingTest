# # TODO 틀림
#
# import math
# from collections import deque
#
# dRow = [0, 1, 0, -1]
# dColumn = [1, 0, -1, 0]
# dDiagonalRow = [1, 1, -1, -1]
# dDiagonalColumn = [1, -1, -1, 1]
#
# def find(board, str):
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == str:
#                 return [i, j]
#
# def bfs(board, r, c, tR, tC):
#     q = deque()
#     distance = [[math.inf] * len(board[i]) for i in range(len(board))]
#     q.append([r, c, 0])
#     distance[r][c] = 0
#
#     while q:
#         row, column, cost, = q.popleft()
#         distance[row][column] = cost
#         for i in range(len(dRow)):
#             movedR = row + dRow[i]
#             movedC = column + dColumn[i]
#             if not 0 <= movedR < len(board) or not 0 <= movedC < len(board[0]):
#                 continue
#             if cost + 2 < distance[movedR][movedC]:
#                 distance[movedR][movedC] = cost + 2
#                 q.append([movedR, movedC, cost + 2])
#         for i in range(len(dDiagonalRow)):
#             movedR = row + dDiagonalRow[i]
#             movedC = column + dDiagonalColumn[i]
#             if not 0 <= movedR < len(board) or not 0 <= movedC < len(board[0]):
#                 continue
#             if cost + 3 < distance[movedR][movedC]:
#                 distance[movedR][movedC] = cost + 3
#                 q.append([movedR, movedC, cost + 3])
#     return distance[tR][tC]
#
# # def solution(numbers):
# #     board = [['1', "2", '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
# #     left = [1, 0]
# #     right = [1, 2]
# #
# #     result = 0
# #     for i in range(len(numbers)):
# #         tR, tC = find(board, numbers[i])
# #         if (left[0] == tR and left[1] == tC) or (right[0] == tR and right[1] == tC):
# #             result += 1
# #             continue
# #         leftCost = bfs(board, left[0], left[1], tR, tC)
# #         rightCost = bfs(board, right[0], right[1], tR, tC)
# #         if leftCost < rightCost:
# #             result += leftCost
# #             left = [tR, tC]
# #         else:
# #             result += rightCost
# #             right = [tR, tC]
# #     return result
#
# result = math.inf
# def dfs(board, numbers, i, left, right, cnt):
#     if len(numbers) == i:
#         global result
#         result = min(result, cnt)
#         return
#
#     tR, tC = find(board, numbers[i])
#     leftCost = bfs(board, left[0], left[1], tR, tC)
#     rightCost = bfs(board, right[0], right[1], tR, tC)
#     if leftCost == 0 and rightCost == 0:
#         dfs(board, numbers, i + 1, [tR, tC], right, cnt + 1)
#         dfs(board, numbers, i + 1, left, [tR, tC], cnt + 1)
#     elif leftCost == 0:
#         dfs(board, numbers, i + 1, [tR, tC], right, cnt + 1)
#     elif rightCost == 0:
#         dfs(board, numbers, i + 1, left, [tR, tC], cnt + 1)
#     elif leftCost == rightCost:
#         dfs(board, numbers, i + 1, [tR, tC], right, cnt + leftCost)
#         dfs(board, numbers, i + 1, left, [tR, tC], cnt + rightCost)
#     elif leftCost < rightCost:
#         dfs(board, numbers, i + 1, [tR, tC], right, cnt + leftCost)
#     else:
#         dfs(board, numbers, i + 1, left, [tR, tC], cnt + rightCost)
#
#
# def solution(numbers):
#     board = [['1', "2", '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
#     left = [1, 0]
#     right = [1, 2]
#
#     dfs(board, numbers, 0, left, right, 0)
#
#     return result


costs = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3]
    , [7, 1, 2, 4, 2, 3, 5, 4, 5, 6]
    , [6, 2, 1, 2, 3, 2, 3, 5, 4, 5]
    , [7, 4, 2, 1, 5, 3, 2, 6, 5, 4]
    , [5, 2, 3, 5, 1, 2, 4, 2, 3, 5]
    , [4, 3, 2, 3, 2, 1, 2, 3, 2, 3]
    , [5, 5, 3, 2, 4, 2, 1, 5, 3, 2]
    , [3, 4, 5, 6, 2, 3, 5, 1, 2, 4]
    , [2, 5, 4, 5, 3, 2, 3, 2, 1, 2]
    , [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]


def solution(numbers):
    now_weight = 0
    left_pos = 4
    right_pos = 6
    all_dict = {}
    finger_pos = (left_pos, right_pos)
    all_dict[finger_pos] = now_weight

    for str_num in numbers:
        num = int(str_num)
        curr_dict = {}
        for finger_pos, weight in all_dict.items():
            left_pos, right_pos = finger_pos
            if right_pos == num:
                if not (left_pos, num) in curr_dict.keys() or curr_dict[(left_pos, num)] > weight + 1:
                    curr_dict[(left_pos, num)] = weight + 1
            elif left_pos == num:
                if not (num, right_pos) in curr_dict.keys() or curr_dict[(num, right_pos)] > weight + 1:
                    curr_dict[(num, right_pos)] = weight + 1
            else:
                if (left_pos, num) not in curr_dict or curr_dict[(left_pos, num)] > weight + costs[right_pos][num]:
                    curr_dict[(left_pos, num)] = weight + costs[right_pos][num]
                if not (num, right_pos) in curr_dict.keys() or curr_dict[(num, right_pos)] > weight + costs[left_pos][num]:
                    curr_dict[(num, right_pos)] = weight + costs[left_pos][num]
        all_dict = curr_dict

    return min(list(all_dict.values()))

print(solution('1756'))
# print(solution('5123'))
# print(solution('1469#76'))
# print(solution('59'))