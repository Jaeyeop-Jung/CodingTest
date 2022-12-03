# TODO 틀림

def solution(words, queries):
    front_dic = {}
    back_dic = {}
    total = {}
    for word in words:
        total[len(word)] = total.get(len(word), 0) + 1
        cur = front_dic
        for i in range(len(word)):
            if word[i] not in cur:
                cur[word[i]] = {}
            cur[len(word) -i] = cur.get(len(word) - i, 0) + 1
            cur = cur[word[i]]

        cur = back_dic
        temp = word[::-1]
        for i in range(len(temp)):
            if temp[i] not in cur:
                cur[temp[i]] = {}
            cur[len(temp) - i] = cur.get(len(temp) - i, 0) + 1
            cur = cur[temp[i]]

    result = []
    for query in queries:
        if query == '?' * len(query):
            if len(query) in total:
                result.append(total[len(query)])
            else:
                result.append(0)
            continue
        if query[0] == '?': # front
            query = query[::-1]
            cur = back_dic
            for i in range(len(query)):
                if query[i] == '?':
                    if len(query) - i in cur:
                        result.append(cur[len(query) - i])
                    else:
                        result.append(0)
                    break
                elif query[i] not in cur:
                    result.append(0)
                    break
                cur = cur[query[i]]

        else:   # back
            cur = front_dic
            for i in range(len(query)):
                if query[i] == '?':
                    if len(query) - i in cur:
                        result.append(cur[len(query) - i])
                    else:
                        result.append(0)
                    break
                elif query[i] not in cur:
                    result.append(0)
                    break
                cur = cur[query[i]]

    return result


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
