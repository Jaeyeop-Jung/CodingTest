# TODO 틀림 https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy

import math
from string import ascii_uppercase

# def solution(name):
#     arr = list(ascii_uppercase)
#     current = 0
#     result = 0
#     for i in name:
#         move = abs(arr.index(i) - current)
#         if arr.index(i) < move:
#             result += 1 + arr.index(i)
#         elif 25 - arr.index(i) < move:
#             result += 1 + (25 - arr.index(i))
#         else:
#             result += move
#         current = arr.index(i)
#     return result

def solution(name):
    # 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min(min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next))

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer


# print(solution("JAZ"))
# print(solution("JEROEN"))
# print(solution("JAN"))
print(solution("JANAAJ"))
