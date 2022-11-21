
def solution(routes):
    routes.sort(key=lambda x: (x[0], x[1]))
    result = 0
    camera = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][1] < camera:
            camera = routes[i][1]
        if routes[i][0] <= camera <= routes[i][1]:
            pass
        else:
            camera = routes[i][1]
            result += 1

    return result + 1


print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))

