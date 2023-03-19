from collections import defaultdict

n = -1
result = []

def dfs(ways, route):
    for way in ways:
        for next, visit in ways[way]:
            if not visit:
                break
        else:
            continue
        break
    else:
        result.append(route)


    for way in ways[route[-1]]:
        next, visit = way
        if not visit:
            way[1] = True
            dfs(ways, route + [next])
            way[1] = False

def solution(tickets):
    global n
    n = len(tickets)
    ways = defaultdict(list)
    for start, end in tickets:
        ways[start].append([end, False])
    dfs(ways, ['ICN'])

    return sorted(result)[0]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))