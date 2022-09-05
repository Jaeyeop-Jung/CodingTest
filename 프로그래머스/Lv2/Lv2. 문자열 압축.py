# TODO 틀림 https://pearlluck.tistory.com/589

def solution(s):
    if len(s) == 1:
        return 1
    answer = 1001
    result = [''] * (len(s) // 2 + 1)
    for i in range(1, len(s) // 2 + 1):
        temp = s[:i]
        cnt = 1
        for j in range(i, len(s) + i, i):
            if temp == s[j:j + i]:
                cnt += 1
            else:
                if cnt == 1:
                    result[i] += temp
                else:
                    result[i] += str(cnt) + temp
                cnt = 1
                temp = s[j:j + i]
        answer = min(answer, len(result[i]))
    print(answer)
    return answer

solution("a")