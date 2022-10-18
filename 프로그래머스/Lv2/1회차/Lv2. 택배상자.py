
def solution(order):
    main, sub = [], []
    cur = 1
    idx = 0
    while len(main) < len(order):
        if cur < order[idx]:
            for i in range(order[idx] - cur):
                sub.append(cur)
                cur += 1

        if cur == order[idx]:
            main.append(cur)
            cur += 1
        elif sub[-1] == order[idx]:
            main.append(sub.pop())
        else:
            break
        idx += 1

    return len(main)


print(solution([4,3,1,2,5]))
print(solution([5,4,3,2,1]))
# print(solution([5,4,2,1,3]))
# print(solution([1,2,3]))
print(solution([]))