
def quadZip(arr, finished, size, result):
    if size < 1:
        return

    # 쿼드 압축 코드
    for i in range(0, len(arr), size):
        for j in range(0, len(arr[i]), size):
            if finished[i][j]:
                continue

            same = True
            num = arr[i][j]
            for r in range(i, i + size):
                for c in range(j, j + size):
                    if num != arr[r][c]:
                        same = False
                        break
                if not same:
                    break
            else:
                for r in range(i, i + size):
                    for c in range(j, j + size):
                        finished[r][c] = True
                        arr[r][c] = -1
                result.append(num)

    # 더 낮은 사이즈 압축
    quadZip(arr, finished, size // 2, result)

    return result

def solution(arr):
    finished = [[False] * len(arr[i]) for i in range(len(arr))]
    result = []
    quadZip(arr, finished, len(arr), result)

    return [result.count(0), result.count(1)]


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))