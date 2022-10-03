
def solution(skill, skill_trees):
    result = 0
    for i in range(len(skill_trees)):
        idx = 0
        flag = False
        for j in range(len(skill_trees[i])):
            if idx != len(skill) and skill_trees[i][j] == skill[idx]:
                idx += 1
            elif idx != len(skill) and skill_trees[i][j] in skill[idx:]:
                flag = True
                break
        if not flag:
            result += 1
    return result


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))