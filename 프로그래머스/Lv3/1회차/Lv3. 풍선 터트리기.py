# TODO 틀림

def solution(a):
    result = 0
    left = [a[0]]
    right = [a[-1]]
    for i in range(1, len(a)):
        if a[i] < left[-1]:
            left.append(a[i])
        else:
            left.append(left[-1])
        if a[-1 - i] < right[-1]:
            right.append(a[-1 - i])
        else:
            right.append(right[-1])
    right.reverse()

    for i in range(1, len(a) - 1):
        if left[i - 1] < a[i] and right[i + 1] < a[i]:
            continue
        result += 1
    return result + 2

print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))