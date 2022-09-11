def solution(n, words):
    temp = {words[0]: 1}
    idx = 1
    while True:
        if len(words) == idx:
            return [0, 0]
        elif words[idx] in temp or words[idx - 1][len(words[idx - 1]) - 1] != words[idx][0]:
            return [idx % n + 1, idx // n + 1]
        temp[words[idx]] = 1
        idx += 1


# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
# print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ['land', 'dream', 'mom', 'mom', 'ror']))
