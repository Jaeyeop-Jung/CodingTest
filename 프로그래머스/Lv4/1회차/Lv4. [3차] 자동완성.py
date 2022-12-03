# TODO 틀림 다음엔 맞출 수 있어


def solution(words):
    words.sort()
    dic = [{}, 0]
    for word in words:
        cur = dic
        for i in range(len(word)):
            if word[i] in cur[0]:
                cur[0][word[i]][1] += 1
                cur = cur[0][word[i][0]]
            else:
                cur[0][word[i]] = [{}, 1]
                cur = cur[0][word[i][0]]

    result = 0
    for word in words:
        cur = dic
        for i in range(len(word)):
            result += 1
            if cur[0][word[i]][1] == 1:
                break
            else:
                cur = cur[0][word[i][0]]

    return result






print(solution(["go","gone","guild"]))
print(solution(["word","war","warrior","world"]))