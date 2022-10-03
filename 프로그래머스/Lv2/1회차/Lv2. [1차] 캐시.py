
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    cache = []
    result = 0
    for i, city in enumerate(cities):
        if not cache:
            cache.append(city)
            result += 5
        elif city in cache:
            cache.remove(city)
            cache.append(city)
            result += 1
        elif len(cache) < cacheSize:
            cache.append(city)
            result += 5
        else:
            cache.pop(0)
            cache.append(city)
            result += 5
    return result

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
# print(solution(2, ["A","B","A"]))


