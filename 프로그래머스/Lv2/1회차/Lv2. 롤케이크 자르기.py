from collections import Counter

def solution(topping):
    result = 0
    allTopping = dict(Counter(topping))
    div = {}
    for i in topping:
        if allTopping[i] == 1:
            del allTopping[i]
        else:
            allTopping[i] -= 1
        div[i] = div.get(i, 0) + 1

        if len(allTopping) == len(div):
            result += 1

    return result

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))