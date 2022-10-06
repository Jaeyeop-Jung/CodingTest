# TODO 틀림

def solution(gems):
    kind = list(set(gems))
    start, end = 0, 0
    result = [1, len(gems)]
    dic = {gems[0] : 1}

    while start < len(gems) and end < len(gems):
        if len(dic) == len(kind):
            if end - start < result[1] - result[0]:
                result = [start + 1, end + 1]
            else:
                dic[gems[start]] -= 1
                if dic[gems[start]] == 0:
                    del dic[gems[start]]
                start += 1
        else:
            end += 1
            if end == len(gems):
                break

            dic[gems[end]] = dic.get(gems[end], 0) + 1

    return result



print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
