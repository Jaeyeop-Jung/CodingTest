
def solution(scores):
    scores = [[scores[i][0], scores[i][1], i] for i in range(len(scores))]
    scores.sort(key=lambda x: (x[0], -x[1]))
    friendScore = scores[-1][1]
    for i in range(len(scores) - 1, -1, -1):
        if scores[i][1] < friendScore:
            if scores[i][2] == 0:
                return -1
            scores.pop(i)
        else:
            friendScore = scores[i][1]

    scores.sort(key=lambda x: -(x[0] + x[1]))
    rank = 0
    curScore = -1
    for i in range(len(scores)):
        if scores[i][0] + scores[i][0] == curScore:
            continue
        else:
            rank += 1
            curScore = scores[i][0] + scores[i][1]
        if scores[i][2] == 0:
            return rank



# print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))
print(solution([[4, 1], [4, 1], [1, 2], [1, 3], [2, 4], [3, 4]]))