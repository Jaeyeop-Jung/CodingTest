# TODO 틀림 구현에 조금 더 집중

def involve(range1, range2):
    if range2[1] <= range1[1]:
        return 0
    if range2[0] <= range1[1] < range2[1]:
        return 1
    return 2

def solution(routes):
    if len(routes) == 1:
        return 1
    result = 1
    routes.sort(key=lambda x: x[0])
    temp = [routes[0][0], routes[0][1]]
    for i in range(1, len(routes)):
        if involve(temp, routes[i]) == 0:
            temp = routes[i]
        elif involve(temp, routes[i]) == 1:
            temp = [routes[i][0], temp[1]]
        else:
            result += 1
            temp = routes[i]
    return result

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))
print(solution([[-100,100],[50,170],[150,200],[-50,-10],[10,20],[30,40]]))