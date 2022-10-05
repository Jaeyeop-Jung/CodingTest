
def solution(genres, plays):
    result = []
    hashMap = {}
    for i in set(genres):
        hashMap[i] = [0]
    for i, playCnt in enumerate(plays):
        hashMap[genres[i]][0] += playCnt
        hashMap[genres[i]].append([playCnt, i])
    popular = sorted([[i, hashMap[i][0]] for i in hashMap], key=lambda x: -x[1])
    for name, _ in popular:
        hashMap[name].pop(0)
        hashMap[name].sort(key=lambda x: (-x[0], x[1]))
        if len(hashMap[name]) == 1:
            result.append(hashMap[name][0][1])
        else:
            result.append(hashMap[name][0][1])
            result.append(hashMap[name][1][1])
    return result


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))