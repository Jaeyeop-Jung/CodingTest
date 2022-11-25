# TODO 틀림 1회차에서는 아이디어도 못 떠올렸는데 이번엔 떠올렸다. 구현을 잘 해봐

# def preOrderLose(arr, involve):
#     if not arr:
#         return
#     for i in arr:
#         involve.add(i)
#         global dic
#         preOrderLose(dic[i][0], involve)
#
# def preOrderWin(arr, involve):
#     if not arr:
#         return
#     for i in arr:
#         involve.add(i)
#         preOrderWin(dic[i][1], involve)
#
# dic = {}
# def solution(n, results):
#     global dic
#     dic = {i: [set(), set()] for i in range(1, n + 1)}
#     for win, lose in results:
#         dic[win][1].add(lose)
#         dic[lose][0].add(win)
#
#     result = 0
#     for key in dic:
#         loses, wins = dic[key]
#         loseSet = set()
#         preOrderLose(loses, loseSet)
#         winSet = set()
#         preOrderWin(wins, winSet)
#         if len(loseSet) + len(winSet) == n - 1:
#             result += 1
#
#     return result


from collections import deque

def solution(n, results):
    dic = {i: [set(), set()] for i in range(1, n + 1)}
    for win, lose in results:
        dic[win][1].add(lose)
        dic[lose][0].add(win)

    result = 0
    for key in dic:
        visited = [False] * n
        visited[key-1] = True
        q = deque()
        q.append(key)
        while q:
            pop = q.popleft()
            for node in dic[pop][0]:
                if not visited[node - 1]:
                    visited[node-1] = True
                    q.append(node)

        q.append(key)
        while q:
            pop = q.popleft()
            for node in dic[pop][1]:
                if not visited[node - 1]:
                    visited[node-1] = True
                    q.append(node)

        if visited.count(True) == n:
            result += 1
    return result

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

