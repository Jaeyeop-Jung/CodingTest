
result = []

def dfs(tickets, visited, n, route):
    visited[n] = True
    if False not in visited:
        global result
        result.append(route[:])
    for i in range(len(tickets)):
        if route[-1] == tickets[i][0] and visited[i] is False:
            route.append(tickets[i][1])
            dfs(tickets, visited, i, route)
            visited[i] = False
            route.pop()

def solution(tickets):
    for i in range(len(tickets)):
        if tickets[i][0] == 'ICN':
            visited = [False] * len(tickets)
            dfs(tickets, visited, i, ['ICN', tickets[i][1]])
    return sorted(result)[0]

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
