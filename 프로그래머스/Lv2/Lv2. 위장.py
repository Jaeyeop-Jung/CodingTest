# TODO 틀림 조합으로 풀면 1번 시간초과
#  https://jjuha-dev.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%9C%84%EC%9E%A5LV2-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

from itertools import combinations

def solution(clothes):
    cloth = {}
    for name, kind in clothes:
        if kind in cloth:
            cloth[kind].append(name)
        else:
            cloth[kind] = [name]

    result = 0
    for i in range(1, len(cloth) + 1):
        for j in combinations(cloth, i):
            temp = 1
            for k in list(j):
                temp *= len(cloth[k])
            result += temp
    return result

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))