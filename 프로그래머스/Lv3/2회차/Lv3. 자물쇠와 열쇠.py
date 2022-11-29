from pprint import pprint

def rotate(key):
    rotate_key = []
    for c in range(len(key)):
        temp = []
        for r in range(len(key) - 1, -1, -1):
            temp.append(key[r][c])
        rotate_key.append(temp)
    return rotate_key

def solution(key, lock):
    n = len(lock)
    board = [[1] * (n * 3) for _ in range(n * 3)]   # 보드 만들기
    for r in range(n, 2 * n):
        for c in range(n, 2 * n):
            board[r][c] = lock[r-n][c-n]

    for i in range(4):
        # 키 돌리고
        key = rotate(key)

        for r in range(len(board) - n):
            for c in range(len(board) - n): # 0, 0부터 마지막까지 탐색
                copy_board = [i[:] for i in board]

                # 키 끼워넣기
                board_row = r
                board_column = c
                for key_row in range(len(key)):
                    for key_column in range(len(key)):
                        copy_board[board_row][board_column] = copy_board[board_row][board_column] ^ key[key_row][key_column]
                        board_column += 1
                    board_row += 1
                    board_column = c

                # 문이 열렸는지 확인
                flag = False
                for row in range(n, 2 * n):
                    for column in range(n, 2 * n):
                        if copy_board[row][column] == 0:
                            flag = True
                            break
                    if flag:
                        break
                else:
                    return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


