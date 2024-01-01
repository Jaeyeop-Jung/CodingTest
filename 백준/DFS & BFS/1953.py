
n = int(input())
arr = [list(map(int, input().split()))[1:] for _ in range(n)]

def dfs(red, blue, idx):
    if idx == n:
        print(len(red))
        print(*sorted(list(red)))
        print(len(blue))
        print(*sorted(list(blue)))
        exit()

    if idx + 1 in red or idx + 1 in blue:
        dfs(red, blue, idx + 1)
    else:
        # blue
        nextBlue = set(list(blue))
        nextRed = set(list(red))
        nextBlue.add(idx + 1)
        for enemy in arr[idx]:
            if enemy in blue:
                break
            flag = False
            for candi in arr[enemy - 1]:
                if candi in nextRed:
                    flag = True
                    break
            if flag:
                break
            nextRed.add(enemy)
        else:
            dfs(nextRed, nextBlue, idx + 1)

        # red
        nextBlue = set(list(blue))
        nextRed = set(list(red))
        nextRed.add(idx + 1)
        for enemy in arr[idx]:
            if enemy in red:
                break
            flag = False
            for candi in arr[enemy - 1]:
                if candi in nextBlue:
                    flag = True
                    break
            if flag:
                break
            nextBlue.add(enemy)
        else:
            dfs(nextRed, nextBlue, idx + 1)


dfs(set(), set(), 0)