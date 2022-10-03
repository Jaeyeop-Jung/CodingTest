# TODO 틀림 https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def solution(n, wires):
    graph = [[] for i in range(n)]
    for i, j in wires:
        graph[i - 1].append(j - 1)
        graph[j - 1].append(i - 1)
    result = 100
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            left = set()
            right = set()
            left.add(i)
            right.add(graph[i][j])
            temp = [[graph[j][i] for i in range(len(graph[j]))] for j in range(len(graph))]
            temp[temp[i][j]].remove(i)
            temp[i].pop(j)
            q = deque(left[0], right[0])
            while q:
                pop = q.popleft()
                for k in range(len(temp[pop])):
                    q.append(temp[pop[k]])


            for k in range(len(temp)):
                for x in range(len(temp[k])):
                    if temp[k][x] in left:
                        left.add(temp[k][x])
                    else:
                        right.add(temp[k][x])
            result = min(result, abs(len(left) - len(right)))
    print(result)




print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# print(solution(4, [[1,2],[2,3],[3,4]]))
# print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))