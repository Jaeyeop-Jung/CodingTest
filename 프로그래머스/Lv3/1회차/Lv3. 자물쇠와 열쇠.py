# TODO 틀림 구현 부분에서 오류가 있는 거 같은데 못잡음

def check(arr):
    m = len(arr) // 3
    for i in range(m, m * 2):
        for j in range(m, m * 2):
            if arr[i][j] != 1:
                return False
    return True

def rotate(arr):
    result = []
    cnt = 0
    while cnt < len(arr[0]):
        result.append([arr[i][cnt] for i in range(len(arr) - 1, -1, -1)])
        cnt += 1
    return result

def solution(key, lock):
    m = len(lock)
    n = len(key)
    board = [[0] * m * 3 for i in range(m * 3)]
    for i in range(m, m * 2):
        for j in range(m, m * 2):
            board[i][j] = lock[i - m][j - m]

    for _ in range(3):
        for i in range(1, m * 2):
            for j in range(1, m * 2):
                temp = [[board[row][column] for column in range(len(board[row]))] for row in range(len(board))]
                for row in range(n):
                    for column in range(n):
                        temp[row + i][column + j] ^= key[row][column]
                if check(temp):
                    return True
        key = rotate(key)
    return False

# print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 1]]))