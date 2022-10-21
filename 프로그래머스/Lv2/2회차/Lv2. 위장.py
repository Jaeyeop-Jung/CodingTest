
def solution(clothes):
    cloth = {}
    for name, kind in clothes:
        cloth[kind] = cloth.get(kind, []) + [name]
    for i in cloth:
        cloth[i].append('-')

    result = 1
    for i in cloth:
        result *= len(cloth[i])
    return result - 1



print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))